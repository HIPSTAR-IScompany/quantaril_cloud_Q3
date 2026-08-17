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
