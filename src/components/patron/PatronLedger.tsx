import ledgerSource from '@site/data/patron/ledger.json';
import PatronBadge from './PatronBadge';
import styles from './styles.module.css';
import type {PatronLedgerRecord} from './types';

const records = [...(ledgerSource.records as PatronLedgerRecord[])].sort((left, right) =>
  (right.occurredAt ?? '').localeCompare(left.occurredAt ?? ''),
);

function quantityLabel(record: PatronLedgerRecord) {
  const {quantity, unit} = record.contribution;
  return quantity === null || unit === null ? null : `${quantity.toLocaleString('ja-JP')} ${unit}`;
}

export default function PatronLedger() {
  if (records.length === 0) {
    return (
      <section className={styles.emptyState} aria-labelledby="patron-ledger-empty-title">
        <p className={styles.kicker}>PUBLIC LEDGER</p>
        <h2 id="patron-ledger-empty-title">公開承認済みの記録を準備しています</h2>
        <p>
          過去の公開感謝記録は候補棚で出典と対象を確認中です。元投稿を読めたことだけで、取引、金額、現在の関係まで確定しません。
        </p>
      </section>
    );
  }

  return (
    <section className={styles.ledgerGrid} aria-label="Patron Ledger">
      {records.map((record) => {
        const quantity = quantityLabel(record);
        return (
          <article className={styles.ledgerCard} key={record.id}>
            <div className={styles.cardTopline}>
              <time dateTime={record.occurredAt ?? undefined}>{record.occurredAt ?? '日付未確定'}</time>
              <PatronBadge mode={record.attribution.mode} />
            </div>
            <h2>{record.attribution.displayName}</h2>
            <p className={styles.arrowLine}>→ {record.contribution.summary}</p>
            <dl className={styles.factList}>
              <div><dt>resource</dt><dd>{record.contribution.resourceType}</dd></div>
              {quantity ? <div><dt>quantity</dt><dd>{quantity}</dd></div> : null}
              <div><dt>scope</dt><dd>{record.scope.join(' / ')}</dd></div>
            </dl>
          </article>
        );
      })}
    </section>
  );
}
