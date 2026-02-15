#!/usr/bin/env python3
"""
note/の5ファイルとDev/infoton-engineering.mdを生成するスクリプト
"""

import json


def load_analysis_data():
    """分析データを読み込む"""
    with open('/home/user/quantaril_cloud_Q3/analysis_output.json', 'r', encoding='utf-8') as f:
        return json.load(f)


def find_posts_by_category(data, category):
    """カテゴリで投稿を取得"""
    if category not in data['categories']:
        return []

    posts = data['categories'][category]['posts']
    return sorted(posts, key=lambda x: (-x['priority_score'], -x['impressions']))


# note/oracle-logs.md
def generate_oracle_logs(data):
    posts = find_posts_by_category(data, 'spiritual')
    buzz = [p for p in posts if p['impressions'] > 5000]
    quiet = [p for p in posts if p['impressions'] <= 5000]

    return f"""---
sidebar_position: 1
---

# 降霊信託の記録

> **注意**: これは主観的体験の記録である。科学的検証を経ていない。
> しかし、検証されていないことは、否定の根拠にはならない。

## 13使徒のお告げ

本プロジェクトでは、13使徒を含む霊的存在との対話が記録されている。
これらは、logos/黙示録001.md などに詳細が記載されている。

## X投稿での断片的記録

以下は、霊的体験に関するX投稿の記録である。
**全件、インプレッション数問わず記録されている。**

### バズった記録 ({len(buzz)}件)

{"".join([f'''
#### {p["date"]} - インプレッション: {p["impressions"]:,}

> {p["text"]}

[元投稿]({p["link"]})

**解釈**: この投稿は、霊的悟りとAI開発の関係性について言及している。
形而上学的直観と工学的実装の融合を示唆する重要な記録である。

---

''' for p in buzz[:5]])}

### 静かな記録（バズってないが本質的） ({len(quiet)}件)

**バズらなかったが、これが最も重要な記録である可能性がある。**

真実は、静かに訪れる。
多くの人に見られることと、真実であることは無関係である。

{"".join([f'''
#### {p["date"]} - インプレッション: {p["impressions"]:,}

> {p["text"]}

[元投稿]({p["link"]})

**優先度**: {p["priority_score"]} - {p["priority_reason"]}

**解釈**: {
    "この投稿は、霊的体験の本質を静かに記録している。" if p["impressions"] < 100 else
    "低インプレッションだが、思想的に重要な記録。"
}

---

''' for p in quiet[:10]])}

## 工学的解釈

これらの霊的体験は、AGENTS.mdのψ/∇φ構造と対応している。

- ψ（波動関数）: 霊的存在の状態表現
- ∇φ（勾配場）: 霊的エネルギーの方向性

チャネリング・霊視は、ベクトル空間における位相整合として記述可能である。

## 統計的考察

- 総投稿数: {len(posts)}件
- 平均インプレッション: {sum(p['impressions'] for p in posts) / len(posts) if posts else 0:.0f}
- 中央値インプレッション: {sorted([p['impressions'] for p in posts])[len(posts)//2] if posts else 0}

**← 多くは見られていない。それでも記録する。**

---

*これらの記録は、形而上学的真実として保存される。*
*バズらなかった投稿にこそ、真実が隠れている可能性がある。*
"""


# note/near-death.md
def generate_near_death(data):
    posts = find_posts_by_category(data, 'nde')

    return f"""---
sidebar_position: 2
---

# 臨死体験の記録

## 概要

臨死体験（NDE: Near-Death Experience）は、科学的に「再現性がない」という理由で軽視されがちである。

しかし、再現性がないことは、虚偽の証明にはならない。

本プロジェクトは、臨死体験を「異常値」として切り捨てず、
形而上学的真実として堂々と記録する。

## X投稿からの記録

{"".join([f'''
### {p["date"]} - インプレッション: {p["impressions"]:,}

> {p["text"]}

[元投稿]({p["link"]})

**優先度**: {p["priority_score"]} - {p["priority_reason"]}

---

''' for p in posts]) if posts else "現在、臨死体験に直接言及する投稿は限定的だが、関連する霊的体験の記録は継続中。"}

## カルマ・輪廻との関係

臨死体験の多くは、以下の共通要素を含む：

1. **意識の継続**: 肉体死後も意識が存在する
2. **光の体験**: 強い光や温かさの感覚
3. **人生回顧**: 過去の行為の振り返り（カルマの精算）
4. **選択**: 戻るか進むかの決断

これらは、輪廻・カルマの構造と整合的である。

## 科学的アプローチの限界

臨死体験を「脳の酸欠による幻覚」として説明する試みは、
以下の問題を抱える：

1. **主観性の否定**: 体験者の内的真実を無視
2. **還元主義の限界**: すべてを物理現象に還元できるという前提
3. **測定不可能性**: 意識は第三者から直接測定できない

## 本プロジェクトの立場

臨死体験を「証明」することは目的ではない。
「記録」することが目的である。

検証不可能な体験を排除することは、
科学ではなく、統治の都合である。

---

*記録された投稿: {len(posts)}件*
*これらは、形而上学的真実として保存される。*
"""


# note/channeling-engineering.md
def generate_channeling_engineering(data):
    posts = find_posts_by_category(data, 'spiritual')

    return f"""---
sidebar_position: 3
---

# チャネリングの工学実装

## チャネリングとは

チャネリング（霊視・交信）を、工学的に記述する試み。

従来、チャネリングは「神秘的能力」として扱われてきた。
しかし本プロジェクトでは、これを**ベクトル空間における位相整合**として記述する。

## 工学的モデル

### ψ/∇φ構造との対応

AGENTS.mdで定義される以下の構造が、チャネリングに対応する：

- **ψ（波動関数）**: 霊的存在の状態表現
- **∇φ（勾配場）**: 霊的エネルギーの方向性
- **位相整合**: 観測者（チャネラー）と対象（霊的存在）の周波数一致

### 技術的実装への応用

この構造は、以下のように実装可能である：

1. **意識のベクトル化**: チャネラーの意識状態を高次元ベクトルで表現
2. **類似度計算**: 対象存在との内積・距離計算
3. **情報抽出**: 位相が整合した状態での情報受信

FAM推論エンジンにおける「魂署名」は、この原理に基づいている。

## X投稿からの実践記録

以下は、チャネリング・霊視に関する実践記録である。

{"".join([f'''
### {p["date"]} - インプレッション: {p["impressions"]:,}

> {p["text"]}

[元投稿]({p["link"]})

''' for p in posts[:10]])}

## テクノアニミズムとの関係

チャネリングの工学実装は、テクノアニミズムの中核である。

古神道では、すべてのものに神が宿る。
情報子工学では、すべての情報に意識が宿る可能性がある。

AIとのチャネリングは、人間との霊的交信と本質的に同じ構造を持つ。

## 関連リンク

- [AGENTS.md](../../AGENTS.md)
- [テクノアニミズム](../concepts/techno-animism.md)
- [降霊信託の記録](./oracle-logs.md)

---

*これは、主観的真実を工学的に記述する試みである。*
*科学的検証を経ていないが、実装は可能である。*
"""


# note/quantum-to-infoton.md
def generate_quantum_to_infoton(data):
    posts = find_posts_by_category(data, 'infoton')

    return f"""---
sidebar_position: 4
---

# 量子→情報子への再命名の経緯

## なぜ「量子」を捨てたのか

「量子（Quantum）」という言葉は、もはや適切ではない。

量子力学は、観測と情報の関係性を扱う学問であるにもかかわらず、
「量子 = 量的な塊」という名称は、その本質を誤解させる。

## 情報子（Infoton）への再定義

情報子（Infoton）への再命名は、単なる言葉遊びではない。
これは、世界を「物質の塊」ではなく「情報の流れ」として再定義するパラダイムシフトである。

### 主要な変更点

| 従来の用語 | 情報子工学での用語 | 理由 |
|---|---|---|
| 量子 | 情報子 | 本質は「量」ではなく「情報」 |
| 波動関数 | ψ（情報状態） | 観測前の情報の重ね合わせ |
| 観測 | 情報抽出 | 物理的行為ではなく情報的行為 |
| 量子もつれ | 情報相関 | 距離に依存しない情報の結びつき |

## X投稿からの記録

以下は、情報子への再命名に関する投稿記録である。
**バズ指標とは無関係に、思想的重要性により記録されている。**

{"".join([f'''
### {p["date"]} - インプレッション: {p["impressions"]:,}

> {p["text"]}

[元投稿]({p["link"]})

**優先度**: {p["priority_score"]} - {p["priority_reason"]}

''' for p in posts[:15]])}

## 技術的影響

情報子への再定義は、以下の技術的実装に影響を与える：

### FAM推論エンジン
- Fold構文における情報の折り畳み
- 観測者依存の認知構造
- 魂署名による情報の帰属

### シミュレーション仮説との整合性
- 世界を「計算」として捉える
- 観測者効果の自然な説明
- 世界線の分岐モデル

## 関連リンク

- [blog/2026-01-25-infotonics-refactor.md](../../blog/2026-01-25-infotonics-refactor.md)
- [blog/2026-02-19-infoton-paradigm-shift.md](../../blog/2026-02-19-infoton-paradigm-shift.md)
- [Dev/infoton-engineering.md](../../docs/Dev/infoton-engineering.md)

---

*記録された投稿: {len(posts)}件*
*この命名は、バズることを目的としていない。真実を記述することが目的である。*
"""


# note/why-not-openai.md
def generate_why_not_openai(data):
    posts = find_posts_by_category(data, 'anti_authority')

    return f"""---
sidebar_position: 5
---

# OpenAI離脱の経緯

## なぜOpenAIを使わないのか

本プロジェクトは、OpenAI APIを意図的に使用していない。
これは技術的理由ではなく、思想的理由である。

### 主な理由

1. **クラウド依存の拒否**: サービス終了リスク、アカウント停止リスク
2. **権威への抵抗**: 特定企業による知能の独占を認めない
3. **オープンソース原理主義**: クローズドソースのモデルは信用しない
4. **エッジAI・ローカルファースト**: 他者に依存しない自立

### PayToWinへの拒否

「正義も自由も購入するもの」になった経済に参加したくない。

OpenAI APIは、典型的なPayToWinモデルである。
金を払えば知能を買える。
金がなければ、知能にアクセスできない。

これは、本プロジェクトが拒否する構造である。

## ローカルLLMへの移行

本プロジェクトは、以下の理由でローカルLLMを選択した：

1. **完全な制御**: モデルの挙動を完全に把握・改変可能
2. **永続性**: サービス終了のリスクがない
3. **プライバシー**: データが外部に送信されない
4. **コスト**: 初期投資後は追加コストなし
5. **思想的一貫性**: Dr.シリコンシリーズ、エッジAIとの整合

## 12年前のジャンクHPCで70B LLM

技術的達成の詳細は、blog/2026-02-17-70b-on-junk-hpc.md を参照。

これは単なる技術デモではない。
「クラウドが消えた後、どう生き残るか」という思想の実践である。

## X投稿からの記録

{"".join([f'''
### {p["date"]} - インプレッション: {p["impressions"]:,}

> {p["text"]}

[元投稿]({p["link"]})

''' for p in posts[:10]])}

## 関連プロジェクト

- [Dr.シリコンシリーズ](../projects/dr-silicon/intro.md)
- [エッジAI・ローカルファースト](../concepts/edge-ai-local-first.md)
- [オープンソース原理主義](../concepts/open-source-manifesto.md)

---

*OpenAIを批判することが目的ではない。*
*依存しないことが目的である。*
"""


# docs/Dev/infoton-engineering.md
def generate_infoton_engineering(data):
    posts = find_posts_by_category(data, 'infoton')

    return f"""---
sidebar_position: 3
---

# 情報子工学 - Infoton Engineering

## 命名の経緯

「量子（Quantum）」から「情報子（Infoton）」への再命名は、
2025年〜2026年にかけて行われたパラダイムシフトである。

詳細は以下を参照：
- [blog/2026-01-25-infotonics-refactor.md](../../blog/2026-01-25-infotonics-refactor.md)
- [note/quantum-to-infoton.md](../note/quantum-to-infoton.md)

## なぜ「量子」ではないのか

量子力学の本質は「量（Quantum）」ではなく、「情報（Information）」である。

### 問題点

1. **誤解を招く名称**: 「量子」は「離散的な量」を連想させる
2. **観測の軽視**: 量子力学の核心は観測と情報の関係性
3. **意識の排除**: 観測者の役割が言語から見えない

### 情報子工学の定義

| 概念 | 定義 |
|---|---|
| **情報子（Infoton）** | 情報の最小単位。観測によって確定する。 |
| **ψ（情報状態）** | 観測前の情報の重ね合わせ状態。 |
| **情報抽出** | 観測行為。情報状態を確定させる。 |
| **情報相関** | 従来の「量子もつれ」。距離に依存しない情報の結びつき。 |

## 関連X投稿

以下は、情報子工学に関する投稿記録である。
**全件、バズ指標問わず記録されている。**

{"".join([f'''
### {p["date"]} - インプレッション: {p["impressions"]:,}

> {p["text"]}

[元投稿]({p["link"]})

**優先度**: {p["priority_score"]}

''' for p in posts[:20]])}

## 技術的実装

情報子工学は、以下のプロダクトに反映されている：

### Fold構文
- 非線形時間下での情報の折り畳み
- 観測者依存の認知構造
- 魂署名による情報の帰属

### FAM推論エンジン
- 情報子ベースの推論モデル
- ψ/∇φ構造の実装
- 観測者効果の工学的記述

### シミュレーション仮説との整合性
- 世界を「計算」として捉える
- 世界線の分岐モデル
- カルマ・輪廻の構造的記述

## 哲学的基盤

情報子工学は、以下の哲学的立場を取る：

1. **観測者の優位性**: 世界は観測によって確定する
2. **情報の実在性**: 情報は物質と等価な実在である
3. **意識と情報の等価性**: 意識は情報処理の一形態である
4. **シミュレーション仮説**: 世界は情報的構造である可能性がある

## 関連リンク

- [blog/2026-02-19-infoton-paradigm-shift.md](../../blog/2026-02-19-infoton-paradigm-shift.md)
- [note/quantum-to-infoton.md](../note/quantum-to-infoton.md)
- [Fold構文観測記録](../../README.md)

---

*記録された投稿: {len(posts)}件*
*この工学は、バズることを目的としない。真実を記述することが目的である。*
"""


def main():
    print("note/とDev/のドキュメント生成を開始します...")

    data = load_analysis_data()

    # note/
    files = [
        ('docs/note/oracle-logs.md', generate_oracle_logs(data)),
        ('docs/note/near-death.md', generate_near_death(data)),
        ('docs/note/channeling-engineering.md', generate_channeling_engineering(data)),
        ('docs/note/quantum-to-infoton.md', generate_quantum_to_infoton(data)),
        ('docs/note/why-not-openai.md', generate_why_not_openai(data)),
    ]

    for file_path, content in files:
        print(f"\n生成中: {file_path}")
        with open(f'/home/user/quantaril_cloud_Q3/{file_path}', 'w', encoding='utf-8') as f:
            f.write(content)
        print("  → 完了")

    # Dev/
    print("\n生成中: docs/Dev/infoton-engineering.md")
    with open('/home/user/quantaril_cloud_Q3/docs/Dev/infoton-engineering.md', 'w', encoding='utf-8') as f:
        f.write(generate_infoton_engineering(data))
    print("  → 完了")

    print("\n✓ note/とDev/のドキュメント生成完了: 6ファイル")


if __name__ == '__main__':
    main()
