#!/usr/bin/env python3
"""
projects/の3シリーズのドキュメントを生成するスクリプト
"""

import json
from datetime import datetime


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


def generate_project_fapta(data):
    """プロジェクトファプタのドキュメントを生成"""
    posts = find_posts_by_category(data, 'project_fapta')

    content = """---
sidebar_position: 1
---

# プロジェクトファプタ - FIATのサービス終了

## 概要

FIATはサービス終了する。これは陰謀論ではなく、構造分析である。

法定通貨（Fiat Currency）は、政府の信用に基づく「サービス」である。
サービスである以上、終了する可能性がある。

歴史的に見れば:
- ハイパーインフレ
- 通貨改革
- デノミネーション
- 金本位制からの離脱

これらはすべて「通貨のサービス終了」の一形態である。

プロジェクトファプタは、この構造的必然性を記録し、
ビットコインをはじめとする非中央集権的通貨への移行を提唱する。

## X投稿アーカイブ

以下は、プロジェクトファプタに関連するX投稿の完全アーカイブです。
**バズった投稿もバズらなかった投稿も全て記録されています。**

"""

    # 全投稿を時系列順に並び替え
    posts_by_time = sorted(posts, key=lambda x: x['date'])

    # バズった投稿
    buzz_posts = [p for p in posts if p['impressions'] > 5000]
    if buzz_posts:
        content += f"### バズった記録 ({len(buzz_posts)}件)\n\n"
        for post in sorted(buzz_posts, key=lambda x: -x['impressions']):
            content += f"#### {post['date']} - インプレッション: {post['impressions']:,}\n\n"
            content += f"> {post['text']}\n\n"
            content += f"[元投稿]({post['link']})\n\n"
            content += "---\n\n"

    # バズらなかった記録
    quiet_posts = [p for p in posts if p['impressions'] <= 5000]
    if quiet_posts:
        content += f"### 地道な記録（バズってないが重要） ({len(quiet_posts)}件)\n\n"
        content += "**これらの投稿は、インプレッション数は低いですが、プロジェクトファプタの思想的コアを形成しています。**\n\n"
        for post in sorted(quiet_posts, key=lambda x: -x['priority_score']):
            content += f"#### {post['date']} - インプレッション: {post['impressions']:,}\n\n"
            content += f"> {post['text']}\n\n"
            content += f"[元投稿]({post['link']})\n\n"
            content += f"**優先度**: {post['priority_score']} - {post['priority_reason']}\n\n"
            content += "---\n\n"

    content += f"""
## 構造分析

複数の投稿を統合した分析により、以下の構造が浮かび上がります:

### 1. 通貨の本質
- FIATは「信用」に基づくサービス
- サービスである以上、終了リスクは常に存在する
- 歴史的に、通貨は何度も「リセット」されてきた

### 2. 現代の兆候
- 米ドル市場とNASDAQの脆弱性
- ハイパーインフレのリスク
- 中央銀行による信用創造の限界

### 3. 構造的必然性
- 債務の指数関数的増大
- 信用創造システムの持続不可能性
- 経済成長の限界

## 歴史的類例

- ワイマール共和国のハイパーインフレ（1923年）
- ジンバブエドルの崩壊（2008年）
- ベネズエラの経済危機（2016年〜）
- アルゼンチンのデフォルト（複数回）

これらはすべて「FIATのサービス終了」の実例である。

## ビットコインへの移行

プロジェクトファプタは、ビットコインを代替案として提唱する理由:

1. **非中央集権**: 政府の信用に依存しない
2. **固定供給**: インフレリスクがない
3. **透明性**: ブロックチェーンによる検証可能性
4. **国境を超える**: グローバルな価値移転

## 関連リンク

- [blog/2026-02-16-project-fapta-endgame.md](../../blog/2026-02-16-project-fapta-endgame.md)
- [docs/concepts/citizen-science.md](../concepts/citizen-science.md)

---

*このドキュメントは、{len(posts)}件のX投稿を完全アーカイブしたものです。*
*バズらなかった{len(quiet_posts)}件の投稿も含まれています。*
"""

    return content


def generate_dr_silicon(data):
    """Dr.シリコンシリーズのドキュメントを生成"""
    posts = find_posts_by_category(data, 'dr_silicon')
    tech_posts = find_posts_by_category(data, 'tech_achievement')
    edge_posts = find_posts_by_category(data, 'edge_ai')

    # 関連投稿を統合
    all_posts = posts + tech_posts + edge_posts
    seen = set()
    unique_posts = []
    for p in all_posts:
        if p['post_id'] not in seen:
            seen.add(p['post_id'])
            unique_posts.append(p)

    unique_posts.sort(key=lambda x: (-x['priority_score'], -x['impressions']))

    content = """---
sidebar_position: 1
---

# Dr.シリコン - When The Cloud Fades

## シリーズ概要

クラウドが消えた後、どう生き残るか。

これは単なるSF的思考実験ではない。
クラウドサービスは、いつでも終了する可能性がある。

- サービス終了
- アカウント停止
- ネットワーク遮断
- 経済崩壊

Dr.シリコンシリーズは、これらのシナリオに備える実践的サバイバル戦略である。

## コンセプト

### When The Cloud Fades

クラウドが消えたとき、何が残るか？

- ローカルに保存されたデータ
- オフラインで動作するソフトウェア
- 自分で修理できるハードウェア
- オープンソースの知識

Dr.シリコンは、これらを統合した「クラウド後の生存戦略」である。

## エピソード・投稿一覧

"""

    if unique_posts:
        content += f"### 技術的達成と実践記録 ({len(unique_posts)}件)\n\n"
        for post in unique_posts[:20]:
            content += f"#### {post['date']} - インプレッション: {post['impressions']:,}\n\n"
            content += f"> {post['text']}\n\n"
            content += f"[元投稿]({post['link']})\n\n"
            if post['keywords']:
                content += f"**キーワード**: {', '.join(post['keywords'][:5])}\n\n"
            if post['impressions'] <= 1000:
                content += "*（バズらなかったが技術的に重要な記録）*\n\n"
            content += "---\n\n"

    content += """
## 技術スタック

### エッジAI
- ローカルLLM（70B on junk HPC）
- CPU推論最適化
- メモリ帯域・スケジューリング・仮想化命令パスの再設計

### ハードウェア
- 12年前のジャンクHPC
- 魔改造ハイパーバイザー
- オープンソースハードウェア

### ソフトウェア
- FAM推論エンジン
- Fold構文
- オープンソース原理主義

### インフラ
- オープンソース古民家
- エネルギー自給
- サバイバルDIY

## 関連プロジェクト

- [オープンソース古民家](../opensource-kominka/intro.md)
- [FAM推論エンジン](../../Dev/)
- [エッジAI・ローカルファースト](../../concepts/edge-ai-local-first.md)

## 関連ブログ記事

- [blog/2026-02-17-70b-on-junk-hpc.md](../../blog/2026-02-17-70b-on-junk-hpc.md)
- [blog/2026-02-20-dr-silicon-when-cloud-fades.md](../../blog/2026-02-20-dr-silicon-when-cloud-fades.md)

---

*このドキュメントは、{len(unique_posts)}件の関連投稿から構成されています。*
"""

    return content


def generate_opensource_kominka(data):
    """オープンソース古民家のドキュメントを生成"""
    posts = find_posts_by_category(data, 'opensource_kominka')
    survival_posts = find_posts_by_category(data, 'survival_diy')

    # 関連投稿を統合
    all_posts = posts + survival_posts
    seen = set()
    unique_posts = []
    for p in all_posts:
        if p['post_id'] not in seen:
            seen.add(p['post_id'])
            unique_posts.append(p)

    unique_posts.sort(key=lambda x: (-x['priority_score'], -x['impressions']))

    content = """---
sidebar_position: 1
---

# オープンソース古民家

## Open Source Hardware Architecture Japan

古民家をハードウェアとして扱う。
設計図をオープンソース化し、誰でも再現可能にする。

## プロジェクト宣言

建築は、コードと同じくオープンソース化できる。
伝統技術は、GitHubで管理できる。

古民家は「文化財」ではなく、「オープンソースハードウェア」である。

### なぜ古民家なのか

1. **再現可能性**: 設計図と工法が明確
2. **修理可能性**: 専用部品に依存しない
3. **持続可能性**: 地産地消の素材
4. **適応可能性**: モジュール化された構造

### なぜオープンソースなのか

1. **知識の民主化**: 誰でもアクセス可能
2. **技術の保存**: 後世に継承可能
3. **改良の自由**: 誰でも改変・再配布可能
4. **独占の排除**: 特定企業・組織に依存しない

## 投稿アーカイブ

以下は、オープンソース古民家プロジェクトに関連するX投稿の完全記録です。

"""

    # バズった記録
    buzz_posts = [p for p in unique_posts if p['impressions'] > 5000]
    if buzz_posts:
        content += f"### バズった記録 ({len(buzz_posts)}件)\n\n"
        for post in sorted(buzz_posts, key=lambda x: -x['impressions']):
            content += f"#### {post['date']} - インプレッション: {post['impressions']:,}\n\n"
            content += f"> {post['text']}\n\n"
            content += f"[元投稿]({post['link']})\n\n"
            content += "---\n\n"

    # 地道な記録
    quiet_posts = [p for p in unique_posts if p['impressions'] <= 5000]
    if quiet_posts:
        content += f"### 地道な記録（バズってないが重要） ({len(quiet_posts)}件)\n\n"
        content += "**実践は静かに進む。バズらなくても、作業は続く。**\n\n"
        for post in sorted(quiet_posts, key=lambda x: -x['priority_score']):
            content += f"#### {post['date']} - インプレッション: {post['impressions']:,}\n\n"
            content += f"> {post['text']}\n\n"
            content += f"[元投稿]({post['link']})\n\n"
            if post['priority_score'] >= 100:
                content += f"**優先度**: {post['priority_score']} - {post['priority_reason']}\n\n"
            content += "---\n\n"

    content += f"""
## 技術要素

### サバイバルDIY
- 極限生活の実践知
- 自給自足の技術
- 焼畑農業などの伝統農法

### 素材工学
- 地産地消の建材
- 伝統的な素材加工技術
- 現代技術との融合

### 縄文技術
- 古代の建築技法
- 自然調和の設計思想
- テクノアニミズムの実践

### エネルギー自給
- 太陽光・風力の活用
- 薪・バイオマスエネルギー
- オフグリッド生活

## Open Source Hardware Architecture Japan（OSHA Japan）の原則

1. **設計図の公開**: すべての設計図をオープンソース化
2. **工法の記録**: 施工プロセスを完全ドキュメント化
3. **素材の標準化**: 誰でも入手可能な素材を使用
4. **改変の自由**: フォーク・改良・再配布を推奨
5. **記名の義務**: クリエイティブ・コモンズに基づく帰属表示

## 関連プロジェクト

- [Dr.シリコンシリーズ](../dr-silicon/intro.md)
- [縄文vs弥生](../../concepts/jomon-vs-yayoi.md)
- [サバイバル実践](../../practice/survival/)
- [伝統工芸](../../practice/traditional-craft/)

## 関連ブログ記事

- [blog/2026-02-21-opensource-kominka-manifesto.md](../../blog/2026-02-21-opensource-kominka-manifesto.md)

---

*このドキュメントは、{len(unique_posts)}件の投稿から構成されています。*
*バズらなかった{len(quiet_posts)}件の地道な記録を含みます。*
"""

    return content


def main():
    print("projects/のドキュメント生成を開始します...")

    data = load_analysis_data()

    # プロジェクトファプタ
    print("\n生成中: docs/projects/project-fapta/intro.md")
    content = generate_project_fapta(data)
    with open('/home/user/quantaril_cloud_Q3/docs/projects/project-fapta/intro.md', 'w', encoding='utf-8') as f:
        f.write(content)
    print("  → 完了")

    # Dr.シリコンシリーズ
    print("\n生成中: docs/projects/dr-silicon/intro.md")
    content = generate_dr_silicon(data)
    with open('/home/user/quantaril_cloud_Q3/docs/projects/dr-silicon/intro.md', 'w', encoding='utf-8') as f:
        f.write(content)
    print("  → 完了")

    # オープンソース古民家
    print("\n生成中: docs/projects/opensource-kominka/intro.md")
    content = generate_opensource_kominka(data)
    with open('/home/user/quantaril_cloud_Q3/docs/projects/opensource-kominka/intro.md', 'w', encoding='utf-8') as f:
        f.write(content)
    print("  → 完了")

    print("\n✓ projectsドキュメント生成完了: 3シリーズ")


if __name__ == '__main__':
    main()
