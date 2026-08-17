---
title: 餌付け
description: 物理送付とwishlistをSFW／NSFW棚に分けて扱う餌付けrouteと将来API境界。
---

# 餌付け

「餌付け」は、ふさもふ活動圏で使われてきた贈与と生存資源の言葉です。食料、飲料、現場差し入れ、制作・生活用品等を、物理送付やAmazonほしい物リスト等の複数channelから置けます。

過去の公開記録にマヨネーズ等への謝意はありますが、現在の募集品、数量、送付先を意味しません。歴史上の募集投稿を現在の不足へ自動変換しません。

## Channel

| channel | 現在の扱い |
|---|---|
| 物理送付 | [公開受取先](./physical)へ送れる現物route |
| Amazonほしい物リスト等 | 既存listをSFW／NSFW別の棚として接続予定。URLはoperator確認後に掲載 |
| API連携 | wishlist、在庫、価格、公開状態等を取得できる場合に将来adapterを実装 |

## SFW／NSFW棚

餌付けのSFW棚とNSFW棚は、同じ一覧へ自動mergeしません。

- `SFW`: 食料、飲料、生活用品、制作・配信・研究資材等
- `NSFW`: 成人向け・身体表現等に隣接する品目を扱う独立棚
- 一つの品目を両棚へ自動複製しない
- NSFW棚への掲載を、SFW棚、支援者、HIPSTAR全体への同意・endorsementへ変換しない
- 閲覧条件、年齢区分、platform policy、配送条件が必要な場合は棚単位で分離する

NSFWをSFWより低い支援階級には置きません。ただし、閲覧者が意図せず別棚へ遷移しないよう、navigationと表示文脈は分けます。

## 今後の棚・API整備

v0.1では、operatorが確認したlist URLを棚ごとに登録できるstatic routeから始めます。将来API連携する場合は、次を別fieldで保持します。

```text
shelfClass: sfw | nsfw
channelType: physical | wishlist | api
platform
label
url
status
observedAt
```

- API、affiliate、埋込み等の利用条件は接続時の公式仕様で確認する
- credential、account ID、非公開list、注文者情報をrepositoryやclient bundleへ置かない
- platform上の価格・在庫は`observedAt`付きの観測値とし、現在値を永続保証しない
- APIが使えない場合も、operator確認済みURLをstatic棚として運用できる
- wishlistの注文・配送情報を公開奉納台帳へ自動転記しない

受取可能な品目、期限、アレルギー、配送条件、公開attributionはchannel／棚ごとに案内します。Amazonほしい物リスト等の実URLとAPI接続は、operatorから公開対象が指定されるまで`USER GATE`です。
