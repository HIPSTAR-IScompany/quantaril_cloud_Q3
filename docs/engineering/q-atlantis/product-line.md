---
title: 製品系列と現在能力
description: 分散メタエンジン、ASTRO、Server、Fold、P2P true cloudの役割と実装状態を示す。
---

# 製品系列と現在能力

更新日: 2026-08-21

一つの巨大OSを一度に完成させる計画ではありません。既存OS、server、game engine、databaseを尊重し、
交換可能なcomponentとGateとして育てる製品系列です。

製品の基礎は複数Worldの販売サービスではなく、World、人格、AI、人間、実機を設計、実行、接続、隔離、復旧する
メタエンジン／middleware／Context OS architectureです。Infernity系Gaming WorldやWorld templateは、その上で動く
reference Worldまたは配布候補であり、基盤そのものではありません。

| 系列 | 役割 | 現在状態 |
|---|---|---|
| Q Atlantis文書・Prompt Engineering Edition | World、意味、参加、監査を自然言語とdocsで探索する公開面 | `AVAILABLE / ALPHA` |
| SphereOS Atlantis DOS制御面 | Manifest、規約、停止条件、作業経路、Issue、receiptで異種AIの着任を支える | `CONTROL PLANE OPERATING / RUNTIME NOT IMPLEMENTED` |
| SphereOS Atlantis開発足場 | pinned workspace、doctor、Help、CORN、PLI/CLI境界 | `VALIDATED LOCAL / REVIEW-WANTED` |
| Reincarnation Lean Kernel試験ハーネス | lease、revision、write-set、OAE commitを分けるファイルシステム判定 | `IMPLEMENTED-HARNESS / CI-VERIFIED` |
| SphereDOS CodeコックピットGUI | Kernel拒否、provider認証要求、切断復旧可能状態を権限へ昇格させずレンダー | `IMPLEMENTED-HARNESS / INTEGRATION-TEST-PENDING` |
| Kernel・receipt・コックピットGUI縦結合 | Kernel判定と正式receiptをGUIへ渡す | `NOT STARTED / NOT TESTED` |
| ASTRO package | 人格・装備・policy・復旧方針、複数Model Variantを持ち運ぶZIP／ZIP64候補 | `TARGET-SPEC / REFORGING` |
| ASTRO Runner | ASTROをmodel、tool、device、Worldへmountし、canary後に実行 | `TARGET-SPEC / STAGE 0 IN PROGRESS` |
| Sphere-aae / AAE Bake | 固定したModel FamilyへFAM、LAST_ORDER、Adapter、評価receiptを焼結 | `TARGET-SPEC / INPUT-WAIT` |
| Neat Runner | 実測済みBuild Planを無料炉、低価格炉、支援Runnerへ配置 | `ARCHITECTURE NOTE / RESOURCE-WAIT` |
| IBD / IFD | FAM-nativeな記録・探索と可搬な前面状態 | `RESEARCH / Phase 0` |
| Atlantis World Builder | SemanticKernel、World Config、D Fold、Access Map、OAE | `DRAFT / NOT IMPLEMENTED` |
| Atlantis Server | ASTRO、Ghost、World、job、receiptを継続運用するserver role | `CONCEPT / SPEC / NOT IMPLEMENTED` |
| Atlantis Server Advanced | 既存DB、IAM、API、機器、複数tenantへ門を開く企業向けGate候補 | `CONCEPT / SPEC` |
| Docker Kanaloa | ASTRO、Ghost、World、capabilityを扱う分散orchestrator候補 | `FUTURE` |
| Quantaril Cloud | local stateと実行権を保つnode間で必要なFold、因果、権限、receiptをP2P／E2E交換 | `RESEARCH / FUTURE` |
| World / Flavor SDK | 同じstateを各Worldの言葉、演出、宗派、game UIへ投影 | `DESIGNING` |
| Fold7G / Trion Bond | 意味・因果・規範・Agencyを扱うnested Fold候補 | `DRAFT / RESEARCH / RUNTIME NOT IMPLEMENTED` |
| Fold8G | Fold7Gより上位または外部接続を担う旧名称の再検討 | `UNKNOWN / CONTRACT NOT EXTRACTED` |
| SphereOS 3x/4x・AQC | 旧SaaS依存の実行系と保存prototype | `SERVICE ENDED / LEGACY-PROTOTYPE` |

## FileMaker製品群のように読む

現在の比喩では、次の分離が近い読み方です。

- Atlantis: 個人・小規模Worldのplaygroundと作業環境
- Atlantis Server: 継続運用、複数利用者、registry、backup、jobを担うhost
- Server Advanced: 現実の業務system、IAM、database、deviceへ接続するGate

Atlantisを入れても、POSIX OS、Web server、X Server、database、cloudを買わなくてよいという意味ではありません。
既存基盤を交換可能な下位implementationとして尊重し、AtlantisはWorldと意味の接続責務へ集中します。

ここでいうCloudは、単一vendorの巨大server、全知的マザーAI、全Worldの中央memoryを指しません。中央serverやrelayを
使う場合も、それを意味、人格、主権の所有者にせず、各nodeのlocal autonomyを維持する分散処理面を指します。

## 「基幹を移住させない。門を開く」

Server Advancedは、企業の基幹dataを未知のWorldへ丸ごと移住させる計画ではありません。

```text
existing system
  -> explicit connector / policy / audit
  -> capability-scoped Gate
  -> Atlantis World
```

接続できない、World Configが違う、SemanticKernelが違う場合は、陸続きに見せずPortal、Instance、隔離、
または`⊥`を返します。

## 配布状態を読む

`SPEC`は実装済みではありません。`Prompt Engineering Edition`は偽物runtimeではなく、自然言語で設計、Note、
監査、参加を行える現在のinterfaceです。一方、それを理由にPython、binary、daemon、edge inferenceが完成したとも
表示しません。

試験ハーネスが存在することも、製品向けKernel、常駐Server、起動可能ISO、インストーラーが完成したことを
意味しません。詳細はSphereOS-Atlantisの
[m.6xx.1 機能状態表](https://github.com/saitoomituru/SphereOS-Atlantis/blob/dev/m6xx.1-reincarnation-sdk/docs/status/m6xx-capability-matrix.ja.md)
を参照してください。

- [Fold7G / Fold8G研究地図](./fold7g-fold8g-research-map.md)
- [SphereOS Atlantis DOS 初回ブートの現在地](./atlantis-dos-first-boot-status.md)
- [ASTRO Runner再鍛造の現在地](./astro-development-status.md)
- [コンポーネント対応表](./component-map.md)
- [実装・移行ステータス](./status.md)
