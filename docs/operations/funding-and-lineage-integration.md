---
title: Q Atlantisの資金・系譜実装契約
description: Manifest正本をQ Atlantisの支援面、fork、商用利用、lineage claim、神聖なNSFWへ適用する。
---

# Q Atlantisの資金・系譜実装契約

- Status: `REPOSITORY-INTEGRATION / PUBLIC-POLICY`
- Updated: 2026-08-17
- Canonical revision observed: `ZeroRoomLab-manifest#8 / 53fb377e`

この文書は、ZeroRoomLab-manifestの横断方針を、Q Atlantisの公開サイト、repository、支援面、派生productへどう適用するかを定めます。正本の機械的な複製ではなく、Q Atlantis固有のadapterです。

## 現在の支援面

| 入口 | 現在の意味 | 意味しないもの |
|---|---|---|
| トップページのPayPal | 置賜郡射程の文化保護NPO・地域活動への公開カンパ | Q Atlantis単体への直接投資、持分購入、用途指定 |
| [Patron Ledger / 奉納台帳](/patron/) | HIPSTAR／Q Atlantis基盤、現物、餌付け、玉垣、Commons linkoutを分け、Human review後にHIPSTAR保有のStripe決済ゲートへ接続するprovenance UI | テキスト確定前の課金開始、個人財布への接続、Patron ranking、取引・金額の自動証明 |
| X経由の直接相談 | 齋藤みつる本人への贈与・現物相談の連絡路 | 作者側からの個別ギフト券勧誘、公開場所での秘密情報受領 |
| Non-Exclusive Seed Steward | 長期責任を用途・期間・上限等で分けて支える契約前方針 | 現在募集済みの証券、株式、債権、返済商品 |

[公開カンパとNon-Exclusive Seed Stewardの説明](/about/stewardship)は、支援前に読める単体Presentationです。

Patron routeの決済非接続は暫定Gateであり、恒久方針ではありません。公開テキスト、受付条件、価格、役務scopeのHuman review完了後、HIPSTARが保有するStripe決済ゲートを接続します。merchant／決済契約／売上受領主体はHIPSTARであり、齋藤みつる個人の決済資産・個人財布へ帰属させません。credential、processor transaction ID、顧客情報、chargeback情報は非公開境界に保持し、公開Ledgerへ自動投影しません。

## 資金で動かさないもの

支援の有無や金額で、Q Atlantisの上流方針、創作、研究、信仰、技術上の意思決定を変更しません。

- 上流、神話、創業者、コミュニティを所有させない
- 金額を議決権、拒否権、編集権、公開停止権へ変換しない
- 特定cloud、model、決済、app storeへ排他固定しない
- 投資家都合で合法なNSFW、身体、豊穣、神楽をSFW漂白しない
- 小口支援者、地域NPO、創業者個人へ研究所全体の損失を押し戻さない

## 分けて背負える責任

一人のPatronが全責任を背負う必要はありません。用途、期間、金額、損失上限、Stage、設備、法務、保存、生活防衛等で責任を区切り、複数Patronが並行して支えられます。

Patron自身も、Q Atlantis以外の研究所、OSS、芸術、startupへ支援portfolioを分散できます。非独占は、上流だけでなく支援者の資金配分にも適用します。

用途限定、段階払い、停止条件、公開receipt、決済紛争処理、保険等は、探索主体を市場から除外するためではなく、リスクを観測・分割・停止・回復可能にするために使います。

## 芳名台帳

支援が実際にbranchや出来事を起動した場合、GitHub、Web、制作日誌、映像、配信、神話等へprovenanceを残すことがあります。

芳名台帳は来歴です。それ以上でも、それ未満でもありません。

- 広告枠ではない
- 露出保証ではない
- 金額による票ではない
- 公式性・正統性・教義決定権ではない
- 成果、利益、返済の保証ではない

過去ソーシャルの感謝投稿は、まず`user-provided-screenshot / screenshot-only`のimport候補として保持します。元URL、target、公開attribution、privacyを確認するまで公開Ledgerへ自動反映せず、投稿が存在したことを`transactionVerified`や金額証明へ変換しません。媒体表示回数も`observedAt`とsourceが揃うまでpublic media recordへ昇格させません。

## fork・Remix・商用product

個別ファイルの表示を優先し、基本境界を次のように扱います。

1. Apache-2.0と表示されたcode・SDKは、その条件に従いfork、改変、配布、商用利用、proprietary productへの組込みができる。
2. CC BYと表示された神話、world flavor、文章、図式は、記名等の条件に従い翻案、再演、別world化、商用利用ができる。
3. black-box model、platform、SDK、cloud、gameを作れる。
4. `built with`、`uses`、`derived from`、`inspired by`等の事実に合う出典表示に、lineage認証は要らない。
5. 上流への許可申請、支援金、思想や収益modelへの同意を一律条件にしない。

個別契約または適用法に別の定めがない限り、上流は独立した下流productの設計、運用、品質、適法性、顧客対応、損失、製造物・service上の責任を引き受けません。

第三者の一方的な組込み、改造、製造、表示、販売、引渡しによって、上流との製造委託、共同製造、OEM、完成品保証、無制限補償契約は成立しません。Patron routeでは、製造物としての安全保証、認証、製造保険、recall、事故対応等、製造責任が必要な責務を最初から受付・履行・保証しません。これはApache-2.0等が許すdownstream利用を追加制限する規則ではなく、利用自由と上流が受付・提供する役務scopeを分離する境界です。

どの依頼・用途が製造責任を必要とする範囲に入るかは、[消費者庁 製造物責任法Q&A](https://www.caa.go.jp/policies/policy/consumer_safety/other/pl_qa.html)を確認するよう案内します。該当する責務が必要な依頼は受付対象外とし、判断が難しい場合も、製造責任を含まないことが確認できるまで受付を開始しません。Q Atlantisのpolicyを絶対免責にも、第三者要求による責任追加oracleにも使いません。

## 正当後継designation

次のような所属・正統性claimを自ら選ぶbundleだけが、Open Lineage designationの対象です。

- `official-lineage`
- `正当後継`
- `orthodoxy`
- `canonical-compatible`
- `lineage-compatible MAGI`
- 同じ流派、公式互換、公式神託等の同義表現

claimの根拠を追試するため、実際のmodelと版・重み・adapter、prompt、検疫、監査、tool、RAG、参照文書、schema、routing、test、失敗例、provenance、build条件、人間overrideを含む完全bundleをShareAlike条件で開きます。

これはApache-2.0 / CC BYを遡及的に再ライセンスする規則ではなく、任意designationの参加条件です。designationを選ばないclosed productは独立した商品・worldであり、劣等を意味しません。

## 神聖なNSFW

Q Atlantisは、合法なNSFW、性愛、裸体、身体、豊穣、生殖、挑発、笑い、宴、神楽をSFWより低い文化カテゴリとして扱いません。

この縄文2.0の信仰では、アメノウズメの神楽が日本と今日の天皇陛下へ連なる御祖先を救ったことをLayer Bで言い切ります。年齢区分、同意、法域、表示、アクセス制御、配布・決済経路は実装できますが、経路制約を原典・信仰・文化的格の劣位へ変換しません。

[Q Atlantisの信仰・工学境界](../philosophy/jomon-2.0-japan-gestalt-and-uzume.md)と、Aboutの[岩戸を開く身体](/about/uzume-and-japan)を参照してください。

## Honest status / User Gate

この方針は、Q Atlantisが完成済みOSであること、金融商品が現在openであること、支援者が露出や神話内の役を得ることを意味しません。

次は個別案件が発生した時点のUser Gateです。

- 法人格、会計主体、税務、KYC、証券性、返済、補償
- 金額、用途、期間、損失上限、停止条件
- 個別の画像、音声、人格、NSFW作品、商標、名称の権利
- lineage designationのauthorityとclaim scope

`unknown` は適合判定ではありません。採用法域と別契約・receiptなしに先回りして確定しません。

## 横断正本

- [資金・創設責任index](https://github.com/saitoomituru/ZeroRoomLab-manifest/blob/main/docs/funding/README.ja.md)
- [Non-Exclusive Seed Steward](https://github.com/saitoomituru/ZeroRoomLab-manifest/blob/main/docs/funding/non-exclusive-seed-steward.ja.md)
- [Open Lineage / Fork / 正統性ポリシー](https://github.com/saitoomituru/ZeroRoomLab-manifest/blob/main/docs/funding/open-lineage-and-fork-policy.ja.md)
- [贈与コモンズ・系譜・局所World拡張契約](https://github.com/saitoomituru/ZeroRoomLab-manifest/blob/main/docs/operations/gift-commons-lineage-and-local-world-extension.ja.md)
- [縄文2.0、日本ゲシュタルト、アメノウズメとNSFW神楽](https://github.com/saitoomituru/ZeroRoomLab-manifest/blob/main/docs/philosophy/jomon-2.0-japan-gestalt-and-uzume.ja.md)
