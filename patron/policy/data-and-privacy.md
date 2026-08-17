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

将来の課金は、公開テキストと受付条件のHuman review後、HIPSTAR保有のStripe決済ゲートへ接続します。決済契約と決済処理の主体はHIPSTARであり、作者個人の決済資産として扱いません。processor上の顧客情報、transaction ID、支払手段、請求・紛争情報を公開奉納台帳へ自動転記せず、公開recordには承認された表示名、target、公開可能なprovenanceだけを分離して投影します。

同様に、公開record、Issue、Patronage、source codeの利用は、製造委託、共同製造、製品保証、事故対応、無制限補償の受付証拠ではありません。HIPSTAR／Q Atlantisは製造責任が必要な責務を受付・履行・保証しません。どの範囲が該当するかは、消費者庁の公式Q&Aへ案内する[Scope and liability](./scope-and-liability)を参照してください。
