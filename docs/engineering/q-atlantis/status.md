---
title: 実装・移行ステータス
---

# 実装・移行ステータス

更新日: 2026-08-21

全体凍結ではありません。開発入口は開いていますが、runtimeとedge実装の火力は不足しています。
現在の全体表示は`OPEN / RESOURCE-WAIT / REVIEW-WANTED`です。

| 対象 | 状態 | このサイトで行うこと |
|---|---|---|
| Q3 / SphereOS 3x・4x | `SERVICE ENDED / PARKED-PRESERVED` | サルベージ工程を閉じ、原典、人格、旧仕様、事故、規約を保存 |
| AQC | `VERIFIED-CODE / DEPRECATED` | 系譜と移行可能範囲を記録 |
| IBD | `RESEARCH / Phase 0` | 参照実装と検証結果へ接続 |
| FAM | `SPEC / MULTIPLE-LINEAGES` | 旧実装主張と現行toy modelを分離 |
| SphereOS Atlantis DOS制御面 | `CONTROL PLANE OPERATING / RUNTIME NOT IMPLEMENTED` | 規約、停止条件、資源探索、試験計画、証跡固定の初回ブートを公開 |
| Architect / Bootstrap足場 | `VALIDATED LOCAL / DESIGN-UNDER-REVIEW` | pinned workspaceと開発足場を維持 |
| Reincarnation Lean Kernel試験ハーネス | `IMPLEMENTED-HARNESS / CI-VERIFIED` | ファイルシステム上の判定負例を試験。製品向けKernelではない |
| SphereDOS CodeコックピットGUI | `IMPLEMENTED-HARNESS / INTEGRATION-TEST-PENDING` | GUIレンダー・境界の自動試験18件を確認。実画面の目視確認前 |
| Kernel・receipt・コックピットGUI縦結合 | `NOT STARTED / NOT TESTED` | Kernel判定をGUIへ渡す縦通し試験を残す |
| 起動可能ISO・インストーラー | `NOT IMPLEMENTED / NOT PROVIDED` | 完成版OS配布物として表示しない |
| ASTRO file | `TARGET-SPEC / REFORGING` | ZIP／ZIP64 archive、複数Model Variant、人格Storage、portable profileを整備 |
| ASTRO Runner | `TARGET-SPEC / STAGE 0 IN PROGRESS` | 責務境界とgeneric Simulator buildの記録あり。正式実機receipt待ち |
| Sphere-aae / AAE Bake | `TARGET-SPEC / INPUT-WAIT / NOT IMPLEMENTED` | ASTRO Stage 1／2実測後にModel Familyと成果物を固定 |
| Neat Runner | `ARCHITECTURE NOTE / RESOURCE-WAIT` | Model／runtime／必要火力の実測後にProvider実装を判定 |
| Instance Ghost | `RESEARCH / SPEC` | 分岐履歴と人格原型の境界を整備 |
| Atlantis | `SPEC / REFORGING` | 世界、隔離、復旧、権限の設計 |
| Sphere Context Dimension OS共通契約 | `REVIEW / CANONICAL-CANDIDATE` | Manifest正本候補へ参照接続 |
| Atlantis World Builder profile | `DRAFT / SPEC / NOT IMPLEMENTED` | World Registry、D Fold、Access Map、OAEの適用境界を定義 |
| Fold7G / Trion Bond | `DRAFT / RESEARCH / RUNTIME NOT IMPLEMENTED` | G/D/Agency/DeFold契約を検討 |
| Fold8G | `UNKNOWN / CONTRACT NOT EXTRACTED` | 旧Sourceから責務差分を抽出・反証する |
| MAGI 3D audit Fold profile | `DRAFT / sidecar設計` | 三Positionを多数決にせずInterpretation OAEへ接続 |
| cloudからedgeへのmodule群 | `DESIGN-UNDER-REVIEW / RESOURCE-WAIT` | hardware、費用、実装担当を募る |
| Q Atlantis文書サイト | `BUILD/DEPLOY PIPELINE IMPLEMENTED` | devで検証し、mainで本番deploy |

この表は実装状態を表し、神話、人格、体験の価値を格付けするものではありません。新しい証拠や実装が確認された場合は、正本と来歴を添えて更新します。

6xx開発線の多軸状態はSphereOS-Atlantisの
[m.6xx.1 機能状態表](https://github.com/saitoomituru/SphereOS-Atlantis/blob/dev/m6xx.1-reincarnation-sdk/docs/status/m6xx-capability-matrix.ja.md)
を正本とします。このページはQ Atlantisの読者向け短縮表示であり、実装、結合、検証、梱包、配布、支援を
一語の「完成度」へ丸めません。

`RESOURCE-WAIT`は却下でも凍結でもありません。Note、review、test、既存bug fix、branch実装を持ち込める状態です。
完成していない機能は、火力を持つ第三者が乗れる公開クエストとして残します。

## StatusはOSSの海図

未実装表示は製品価値の否定ではなく、参加者が最初のcommitを置ける未踏領域の座標です。

| 海図の表示 | 持ち込めるplay |
| --- | --- |
| `UNKNOWN / NOT EXTRACTED` | 旧Source探索、比較、反証、責務定義 |
| `DRAFT / SPEC` | review、反例、schema、test case |
| `NOT IMPLEMENTED` | reference実装、adapter、runner、UI |
| `RESOURCE-WAIT` | hardware、電気、費用、時間、運用担当 |
| `REVIEW-WANTED` | 巫女、神学、ゲーマー、当事者、工学者の棚別review |

完成品の客だけでなく、Note、反証、fork、実装、playtest、Supplyを持つOSSパイレーツの乗船を歓迎します。

- [SphereOS Atlantis DOS 初回ブートの観測境界](./atlantis-dos-first-boot-status.md)
