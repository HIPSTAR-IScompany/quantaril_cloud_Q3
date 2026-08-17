import fs from 'node:fs';
import path from 'node:path';
import process from 'node:process';

const repositoryRoot = process.cwd();
const dataDirectory = path.join(repositoryRoot, 'data', 'patron');
const candidatePath = path.join(
  repositoryRoot,
  'sources',
  'patron',
  'import-candidates',
  'social-legacy.json',
);

const publicContracts = new Map([
  ['ledger.json', 'q-atlantis-patron-ledger/1'],
  ['activity.json', 'q-atlantis-patron-activity/1'],
  ['media.json', 'q-atlantis-patron-media/1'],
  ['supply.json', 'q-atlantis-patron-supply/1'],
  ['tamagaki.json', 'q-atlantis-patron-tamagaki/1'],
]);

const forbiddenKeys = new Set([
  'address',
  'bankAccount',
  'bankAccountNumber',
  'homeAddress',
  'invoice',
  'invoiceNumber',
  'paymentProcessorTransactionId',
  'privateDonorIdentity',
  'privateMessage',
  'secret',
]);

const attributionModes = new Set([
  'named',
  'public-handle',
  'anonymous-patron',
  'anonymous-community',
  'anonymous-commons',
  'unknown',
]);
const supplyStatuses = new Set(['UNKNOWN', 'DORMANT', 'LOW', 'STABLE', 'SURPLUS']);
const tamagakiStatuses = new Set(['SCHEDULED', 'ACTIVE', 'RETIRED', 'CANCELLED']);
const candidateClasses = new Set([
  'contribution',
  'collaboration',
  'acknowledgement',
  'activity-evidence',
  'media-observation',
  'supply-request',
]);

const problems = [];

function fail(location, message) {
  problems.push(`${location}: ${message}`);
}

function loadJson(filePath) {
  try {
    return JSON.parse(fs.readFileSync(filePath, 'utf8'));
  } catch (error) {
    fail(path.relative(repositoryRoot, filePath), `JSONを読めません: ${error.message}`);
    return null;
  }
}

function isNullableDate(value) {
  return value === null || /^\d{4}-\d{2}-\d{2}$/.test(value);
}

function isNullableTimestamp(value) {
  return value === null || /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:Z|[+-]\d{2}:\d{2})$/.test(value);
}

function scanForbiddenKeys(value, location) {
  if (Array.isArray(value)) {
    value.forEach((item, index) => scanForbiddenKeys(item, `${location}[${index}]`));
    return;
  }
  if (!value || typeof value !== 'object') return;
  for (const [key, child] of Object.entries(value)) {
    if (forbiddenKeys.has(key)) fail(`${location}.${key}`, 'public dataで禁止されたfieldです');
    scanForbiddenKeys(child, `${location}.${key}`);
  }
}

function validateEnvelope(document, location, schema) {
  if (!document) return false;
  if (document.schema !== schema) fail(location, `schemaは${schema}である必要があります`);
  if (!isNullableTimestamp(document.updatedAt ?? null)) {
    fail(`${location}.updatedAt`, 'nullまたはtimezone付きISO timestampが必要です');
  }
  if (!Array.isArray(document.records)) {
    fail(`${location}.records`, '配列が必要です');
    return false;
  }
  const ids = new Set();
  for (const [index, record] of document.records.entries()) {
    const recordLocation = `${location}.records[${index}]`;
    if (!record || typeof record !== 'object' || Array.isArray(record)) {
      fail(recordLocation, 'objectが必要です');
      continue;
    }
    if (typeof record.id !== 'string' || record.id.trim() === '') {
      fail(`${recordLocation}.id`, '空でない文字列が必要です');
    } else if (ids.has(record.id)) {
      fail(`${recordLocation}.id`, `duplicate id: ${record.id}`);
    } else {
      ids.add(record.id);
    }
  }
  scanForbiddenKeys(document, location);
  return true;
}

function validateAttribution(attribution, location) {
  if (!attribution || typeof attribution !== 'object') {
    fail(location, 'attribution objectが必要です');
    return;
  }
  if (!attributionModes.has(attribution.mode)) {
    fail(`${location}.mode`, `未知のattribution mode: ${attribution.mode ?? 'missing'}`);
  }
  if (attribution.mode === 'unknown' && attribution.displayName !== null) {
    fail(`${location}.displayName`, 'unknown attributionのdisplayNameはnullにします');
  }
  if (attribution.mode === 'public-handle' && !/^@[A-Za-z0-9_]+$/.test(attribution.displayName ?? '')) {
    fail(`${location}.displayName`, 'public-handleは@で始まる公開handleが必要です');
  }
}

function validateContribution(contribution, location) {
  if (!contribution || typeof contribution !== 'object') {
    fail(location, 'contribution objectが必要です');
    return;
  }
  for (const field of ['kind', 'resourceType', 'summary']) {
    if (typeof contribution[field] !== 'string' || contribution[field].trim() === '') {
      fail(`${location}.${field}`, '空でない文字列が必要です');
    }
  }
  for (const field of ['quantity', 'amountJpy', 'valuationJpy']) {
    const value = contribution[field];
    if (value !== null && (!Number.isFinite(value) || value < 0)) {
      fail(`${location}.${field}`, 'nullまたは0以上の有限数が必要です');
    }
  }
  if (contribution.quantity !== null && !contribution.unit) {
    fail(`${location}.unit`, 'quantityを公開する場合はunitが必要です');
  }
  if (contribution.valuationJpy !== null) {
    if (!contribution.valuationMethod) fail(`${location}.valuationMethod`, 'valuationには算定方法が必要です');
    if (!isNullableTimestamp(contribution.valuationObservedAt ?? undefined) || contribution.valuationObservedAt === null) {
      fail(`${location}.valuationObservedAt`, 'valuationには観測timestampが必要です');
    }
    if (!contribution.valuationSourceRef) fail(`${location}.valuationSourceRef`, 'valuationにはsourceRefが必要です');
  }
}

for (const [fileName, schema] of publicContracts) {
  const location = `data/patron/${fileName}`;
  const document = loadJson(path.join(dataDirectory, fileName));
  if (!validateEnvelope(document, location, schema)) continue;

  if (fileName === 'ledger.json') {
    document.records.forEach((record, index) => {
      validateAttribution(record.attribution, `${location}.records[${index}].attribution`);
      validateContribution(record.contribution, `${location}.records[${index}].contribution`);
      if (!isNullableDate(record.occurredAt ?? null)) fail(`${location}.records[${index}].occurredAt`, 'ISO dateまたはnullが必要です');
    });
  }

  if (fileName === 'supply.json') {
    document.records.forEach((record, index) => {
      const recordLocation = `${location}.records[${index}]`;
      if (!supplyStatuses.has(record.status)) fail(`${recordLocation}.status`, `未知のSupply status: ${record.status}`);
      if (!isNullableTimestamp(record.updatedAt)) fail(`${recordLocation}.updatedAt`, 'timezone付きtimestampまたはnullが必要です');
      if (record.status !== 'UNKNOWN' && record.updatedAt === null) fail(`${recordLocation}.updatedAt`, 'UNKNOWN以外は観測timestampが必要です');
    });
  }

  if (fileName === 'tamagaki.json') {
    document.records.forEach((record, index) => {
      const recordLocation = `${location}.records[${index}]`;
      if (!tamagakiStatuses.has(record.status)) fail(`${recordLocation}.status`, `未知の玉垣status: ${record.status}`);
      if (!isNullableDate(record.startsAt) || record.startsAt === null) fail(`${recordLocation}.startsAt`, 'ISO dateが必要です');
      if (!isNullableDate(record.expiresAt) || record.expiresAt === null) fail(`${recordLocation}.expiresAt`, 'ISO dateが必要です');
      if (record.startsAt && record.expiresAt && record.startsAt > record.expiresAt) fail(recordLocation, 'startsAtがexpiresAtより後です');
      if (record.disclosure !== 'sponsored-advertising') fail(`${recordLocation}.disclosure`, '玉垣はsponsored-advertisingを明示します');
    });
  }

  if (fileName === 'media.json') {
    document.records.forEach((record, index) => {
      const recordLocation = `${location}.records[${index}]`;
      for (const field of ['platform', 'metric', 'sourceRef', 'notes']) {
        if (typeof record[field] !== 'string' || record[field].trim() === '') fail(`${recordLocation}.${field}`, '空でない文字列が必要です');
      }
      if (!Number.isFinite(record.value) || record.value < 0) fail(`${recordLocation}.value`, '0以上の有限数が必要です');
      if (!isNullableTimestamp(record.observedAt) || record.observedAt === null) fail(`${recordLocation}.observedAt`, '観測timestampが必要です');
    });
  }
}

const candidates = loadJson(candidatePath);
const candidateLocation = 'sources/patron/import-candidates/social-legacy.json';
if (candidates) {
  if (candidates.schema !== 'q-atlantis-patron-social-import-candidates/1') {
    fail(candidateLocation, '候補schemaが一致しません');
  }
  if (!Array.isArray(candidates.records)) {
    fail(`${candidateLocation}.records`, '配列が必要です');
  } else {
    const ids = new Set();
    candidates.records.forEach((record, index) => {
      const recordLocation = `${candidateLocation}.records[${index}]`;
      if (ids.has(record.id)) fail(`${recordLocation}.id`, `duplicate id: ${record.id}`);
      ids.add(record.id);
      if (!candidateClasses.has(record.recordClass)) fail(`${recordLocation}.recordClass`, `未知の候補分類: ${record.recordClass}`);
      if (record.publicationStatus !== 'candidate') fail(`${recordLocation}.publicationStatus`, '候補棚ではcandidateのみ許可します');
      validateAttribution(record.attribution, `${recordLocation}.attribution`);
      if (record.contribution) validateContribution(record.contribution, `${recordLocation}.contribution`);
      if (!isNullableDate(record.occurredAt ?? null)) fail(`${recordLocation}.occurredAt`, 'ISO dateまたはnullが必要です');
      if (!isNullableDate(record.publishedAt ?? null)) fail(`${recordLocation}.publishedAt`, 'ISO dateまたはnullが必要です');
      if (record.source?.evidenceType !== 'user-provided-screenshot') fail(`${recordLocation}.source.evidenceType`, '現候補はuser-provided-screenshotとして保持します');
      if (record.source?.url !== null) fail(`${recordLocation}.source.url`, '未確認URLを候補へ捏造しません');
      if (record.verification?.status !== 'screenshot-only') fail(`${recordLocation}.verification.status`, '現候補はscreenshot-onlyです');
      if (record.verification?.transactionVerified !== false) fail(`${recordLocation}.verification.transactionVerified`, '取引証明済みへ昇格できません');
      if (record.privacyReview !== 'required') fail(`${recordLocation}.privacyReview`, '公開前privacy reviewが必要です');
    });
  }
  scanForbiddenKeys(candidates, candidateLocation);
}

if (problems.length > 0) {
  console.error(`PATRON_CHECK_FAILED: ${problems.length}件`);
  problems.forEach((problem) => console.error(`  - ${problem}`));
  process.exitCode = 1;
} else {
  const publicRecordCount = [...publicContracts.keys()]
    .map((fileName) => loadJson(path.join(dataDirectory, fileName))?.records?.length ?? 0)
    .reduce((sum, count) => sum + count, 0);
  console.log(`PATRON_CHECK_OK: public ${publicRecordCount} records / candidates ${candidates?.records?.length ?? 0}`);
}
