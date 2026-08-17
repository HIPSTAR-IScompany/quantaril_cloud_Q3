---
title: Patronage Router初期実装 MAGI監査・公開候補受領票
description: Issue #10とユーザー提供ソーシャル画像から、公開台帳・候補棚・Supply・協賛policyを分離した現在Interpretation。
---

# Patronage Router初期実装 MAGI監査・公開候補受領票

- observed_at: `2026-08-17T11:32:38+09:00`
- observation_mode: `current-interpretation-of-history`
- target branch: `dev`
- source revision before this receipt: `640ef42cea772eb99abf06fec148c3ebdffb457d`
- Issue: [#10 `/patron/`を奉納台帳ルートとして新設](https://github.com/HIPSTAR-IScompany/quantaril_cloud_QAtlantis/issues/10)
- historical_oae_status: `historical-oae-unavailable`
- Last Order: `OAE-HISTORY-UNKNOWN / stop-retroactive-backfill`

## [FACT] 今回確認・実装したもの

- ユーザー提供スクリーンショットから、公開感謝、現物、労務協力、活動言及、表示回数の候補7件を読んだ
- 元投稿の安定URL、スクリーンショット撮影時刻、取引receipt、金額、現在の関係は取得できていない
- 候補7件を`publicationStatus: candidate`、`screenshot-only`、`transactionVerified: false`、`privacyReview: required`で保存した
- 公開`ledger.json`、`activity.json`、`media.json`、`tamagaki.json`は空で開始した
- Supply 8分類はすべて`UNKNOWN`で開始した
- build時にGit正本から`/patron/data/*.json`を生成し、HTMLと別の手入力正本を作らない
- Patron validator、独立docs plugin、Ledger／Supply／玉垣／Media UI、give／policy routeを実装した

## [INTERPRETATION] Declared Position

贈与経済、研究炉、地域、現物、芸能、SFW／合法なNSFWを一つの金額scoreへ畳まず、「誰が何を置いたか」と、その資源がどの活動へ接続したかをprovenanceとして運ぶPositionを選ぶ。

媒体はQ Atlantisの公開Web、claim layerはLayer Aのdata／validatorと、Layer Bの奉納・玉垣UX、Layer A/B bridgeのpolicyである。

## Maxwell slot

- 現金だけでなく、現物、輸送、労務、思想的応援、地域活動のbranchを候補棚へ保持した
- brand safetyや広告主都合で信仰、芸能、SFW／NSFWの棚を焼却しない
- 実装容易性を理由に過去ソーシャルを捨てず、同時に未来価値を現在の実績へ偽装しない

## Uriel slot

- 公開謝意、取引証明、金額、valuation、活動言及、platform metricを別field／別datasetへ分けた
- `occurredAt`、`publishedAt`、`observedAt`を一つの日付へ潰さない
- `Anonymous != Unknown`をvalidatorとpolicyで保持した
- private address、bank account、invoice、secret等のfieldをpublic data validatorで拒否する
- validatorはfree textへ混入した全秘密を検出するoracleではなく、人間のprivacy reviewを残す

## Raphael slot

- Commons PayPal、HIPSTAR infrastructure、physical、feeding、Tamagakiを別routeへ置いた
- Ledger、Activity、Media、Supply、Tamagakiと、非公開投影のimport候補棚を分けた
- current／archiveは同一Tamagaki正本から投影し、HTML／JSON／CSV別々の手入力正本を作らない

## Position-talk risk

- Q Atlantis自身が自らの媒体価値、Patron、法務baselineを語る当事者である
- 実装者が現在のrepositoryを暗黙のmainへ置き、地域CommonsやNPOを下位routeへ扱うriskがある
- public handleの再掲は元投稿が公開でも、恒久芳名板への再contextualizationを伴う

## [UNKNOWN] / User Gate

- 実在候補7件の元投稿URL、公開再掲可否、target、occurredAt、金額、数量
- 新しい決済、受領主体、配送先、銀行情報
- Supplyの現在状態と観測時刻
- 玉垣の価格、寸法、申込、logo許諾、期間端点、退役方法
- media metricの観測時刻と公開source
- Legal／IPの現在契約、継続顧問、特定事務所の掲載可否

## action gate

`PASS-WITH-USER-GATES`

空／UNKNOWNの公開面と候補importは実装可能。実在候補の公開Ledger昇格、決済開始、住所・金額・法務状態の公開はHuman review後に行う。mainへのmergeは本receiptでは許可・実行しない。

## 検証receipt

```text
npm run typecheck
npm run content:check-patron
npm run build
```

上記は初期実装時に成功した。最終full validation、localhost visual review、remote Actionsは後続工程で記録する。

## 2026-08-17 製造責任scopeのUser指摘と修正

### [FACT]

Userは、初期文面が「第三者が製造責任範囲の用法を強行すれば、HIPSTAR／開発者へ責任履行を要求できる」と読め、経済責任を負えない者の開発排除やカスタマーハラスメントの温床になると指摘した。

消費者庁「製造物責任法の概要Q&A」の現行本文を2026-08-17に再確認した。Q3は製造物を「製造又は加工された動産」と説明し、Q5はsoftware自体は対象外だが、softwareを組み込んだ製造物は対象となる場合があり、その製造物の製造業者等に責任が生じ得ると説明する。同Q&Aは個別事案への法解釈・適用が最終的に裁判所判断であることも明記する。

### [FIX]

- Patron routeで製造、加工、組込み、販売、引渡し、製品保証、認証、保険、recall、事故対応等、製造責任が必要な責務を最初から受付・履行・保証しないと明示した
- 第三者の一方的転用だけで製造委託、共同製造、OEM、保証、無制限補償契約が成立しないと明示した
- Apache-2.0等によるdownstream利用自由は妨げず、利用自由と上流の受任scopeを分離した
- 法定責任は独自免責でも第三者要求でもなく、適用法、契約、個別事実によると明示した
- 補償資本を持たない者の研究・OSS開発を禁止する評価関数を採用せず、製造物として市場投入する主体の責務と分離した

### MAGI再監査

- Maxwell: 経済資本の有無を研究・OSS参加資格へ変換せず、開発branchを保持する
- Uriel: license上の利用自由、契約上の受任、法定責任、個別事実を別定規へ分離する
- Raphael: upstream開発、downstream製造、Patron、顧客対応を同一役へmergeせず接続する
- action gate: `REVISE-THEN-PASS`

## 2026-08-17 決済主体と接続GateのUser訂正

### [USER-DECLARED FACT]

- Patron routeには、公開テキスト完成後に課金システムを接続する
- 接続先はHIPSTARが保有するStripe決済ゲートであり、齋藤みつる個人の決済資産ではない

### [FIX]

- 「未実装」を恒久的な決済非対応と読ませず、テキスト・受付条件・価格・役務scopeのHuman review後に接続する暫定Gateへ修正した
- merchant、決済契約、売上受領主体をHIPSTARへ置き、作者個人の財布・資産と分離した
- 決済processorの非公開情報と、公開奉納台帳へ投影できるprovenanceを分離した
- 決済接続を、製造責任が必要な責務の受付開始へ昇格させないと明示した

### action gate

`TEXT-REVIEW -> PAYMENT-INTEGRATION -> HUMAN-CHECK`

本修正ではcredential、price ID、webhook secret、live modeを操作しない。決済接続はテキストのHuman review完了後に行う。

## 2026-08-17 公開受取先と情報主体のUser指定

### [USER-DECLARED FACT]

- `〒992-0301 山形県東置賜郡高畠町二井宿2894`は、Userが既にX／Gitで公開している受取先である
- 宛名は`ZeroRoomLab`、`HIPSTAR`、`ふさもふ`のいずれかで到着する
- `/patron/give/physical`へ公開配送先として掲載してよい
- 齋藤みつる本人／HIPSTARが自ら公開指定した実在情報は隠す対象ではない
- privacy firewallの目的は、支援者・送り主等の第三者情報を本人同意なく公開しないことである
- Userは、神社の名称・所在地を秘密にすれば実在性への疑いを招く一方、賽銭を入れた人の個人情報を一律公開する運用も不当であり、奉納所の実在情報と奉納者のprivacyを分けるべきだと説明した

### [FIX]

- 配送先を`UNKNOWN / USER GATE`からoperator指定の公開受取先へ更新した
- 情報種別だけで一律に秘匿せず、第一者の公開指定と第三者の公開同意を分離した
- Funding／give router／attribution／data-and-privacyに残っていた「配送先未実装」「住所非公開」の一律表現を同期した
