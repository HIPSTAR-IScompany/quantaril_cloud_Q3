---
title: Data and privacy
description: 過去ソーシャルから公開奉納台帳へrecordを昇格する検証とprivacy firewall。
---

# Data and privacy

過去ソーシャルの感謝投稿は、実在recordの候補です。ただし、投稿を読めたことと、取引、金額、契約、現在の関係を独立証明できることは別です。

```text
social screenshot
  → import candidate
  → source URL / target / attribution / privacy review
  → approved public record
  → Ledger / Activity / Mediaの各projection
```

候補棚の最低field:

- `recordClass`
- `occurredAt` / `publishedAt` / `observedAt`
- `source.platform` / `account` / `url` / `evidenceType`
- `verification.status` / `claimScope`
- `publicationStatus`
- `privacyReview`

公開しないもの:

- private donor identity
- bank account、home address
- invoice、private legal correspondence
- private DM
- payment processor transaction ID
- 未承認の金額、推定評価額

`screenshot-only`は公開投稿の記載を確認した強度です。`receipt-backed`や`transactionVerified`へ自動昇格しません。
