export type AttributionMode =
  | 'named'
  | 'public-handle'
  | 'anonymous-patron'
  | 'anonymous-community'
  | 'anonymous-commons';

export type PatronLedgerRecord = {
  id: string;
  occurredAt: string | null;
  attribution: {
    mode: AttributionMode;
    displayName: string;
    entityKind: string;
    url?: string | null;
    logo?: string | null;
  };
  contribution: {
    kind: string;
    resourceType: string;
    summary: string;
    quantity: number | null;
    unit: string | null;
    amountJpy: number | null;
    valuationJpy: number | null;
  };
  scope: string[];
  disclosure: string;
  observedAt: string;
  evidence: string[];
};

export type SupplyRecord = {
  id: string;
  label: string;
  status: 'UNKNOWN' | 'DORMANT' | 'LOW' | 'STABLE' | 'SURPLUS';
  updatedAt: string | null;
  note: string | null;
};

export type TamagakiRecord = {
  id: string;
  patronRef: string;
  cycle: string;
  startsAt: string;
  expiresAt: string;
  status: 'SCHEDULED' | 'ACTIVE' | 'RETIRED' | 'CANCELLED';
  label: string;
  logo: string | null;
  url: string | null;
  disclosure: 'sponsored-advertising';
};

export type MediaRecord = {
  id: string;
  platform: string;
  metric: string;
  value: number;
  periodStart: string | null;
  periodEnd: string | null;
  observedAt: string;
  sourceRef: string;
  notes: string;
};

export type PatronService = {
  schema: 'q-atlantis-patron-service/1';
  updatedAt: string;
  status: 'PRELAUNCH' | 'OPEN' | 'PAUSED';
  statusLabel: string;
  applicationsEnabled: boolean;
  checkoutEnabled: boolean;
  earlyContactEnabled: boolean;
  contact: {
    telephone: string;
    telephoneMode: 'voicemail-callback';
    routes: Array<{
      kind: string;
      label: string;
      url: string;
      privacy: 'private-contact' | 'public-intake' | 'follow-channel-guidance';
    }>;
  };
};

export type PatronOffering = {
  id: string;
  label: string;
  availability: 'PRELAUNCH' | 'OPEN' | 'PAUSED' | 'SOLD_OUT';
  priceTaxExcludedJpy: number;
  priceTaxIncludedJpy: number;
  taxRate: number;
  unitCountMin: number;
  unitCountMax: number | null;
  publicDisplayCountPerEntityPerTerm: number;
  plaqueCountPerEntityPerTerm: number;
  physicalSlotLimit: number | null;
  term: {
    mode: 'FROM_PUBLICATION' | 'FIXED_HALF_YEAR';
    months: number | null;
    startsFrom: 'publishedAt' | 'cycleStart';
    status: 'ADJUSTING' | 'CONFIRMED';
    renewalGates?: string[];
  };
  specStatus: 'ADJUSTING' | 'CONFIRMED' | 'NOT_APPLICABLE';
  checkoutEnabled: boolean;
};
