#!/usr/bin/env python3
"""
concepts/の7つの柱のドキュメントを生成するスクリプト
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


def generate_concept_doc(title, sidebar_position, definition, background, category, data, related_projects, related_links):
    """conceptドキュメントを生成"""

    posts = find_posts_by_category(data, category)

    # バズった投稿とバズらなかった重要投稿に分類
    buzz_posts = [p for p in posts if p['impressions'] > 5000]
    quiet_but_important = [p for p in posts if p['impressions'] <= 5000 and p['priority_score'] >= 100]
    other_posts = [p for p in posts if p['impressions'] <= 5000 and p['priority_score'] < 100]

    content = f"""---
sidebar_position: {sidebar_position}
---

# {title}

## 定義

{definition}

## 背景

{background}

## 実例（X投稿より）

本セクションでは、実際のX投稿から抽出した具体例を記録します。
バズった投稿もバズらなかった投稿も、思想的重要性に基づいて等しく扱われています。

"""

    if buzz_posts:
        content += f"### バズった投稿 ({len(buzz_posts)}件)\n\n"
        for post in buzz_posts[:10]:
            content += f"#### {post['date']} - インプレッション: {post['impressions']:,}\n\n"
            content += f"> {post['text']}\n\n"
            content += f"[元投稿]({post['link']})\n\n"
            if post['keywords']:
                content += f"**キーワード**: {', '.join(post['keywords'][:5])}\n\n"
            content += "---\n\n"

    if quiet_but_important:
        content += f"### 重要だがバズらなかった投稿 ({len(quiet_but_important)}件)\n\n"
        content += "**これが重要。バズらなくても真実は真実。**\n\n"
        content += "インプレッション数が低くても、思想的コアに関わる投稿は全て記録されています。\n"
        content += "むしろ、バズらなかった投稿にこそ、本質が隠れている可能性があります。\n\n"

        for post in quiet_but_important[:10]:
            content += f"#### {post['date']} - インプレッション: {post['impressions']:,}\n\n"
            content += f"> {post['text']}\n\n"
            content += f"[元投稿]({post['link']})\n\n"
            content += f"**優先度スコア**: {post['priority_score']}\n\n"
            content += f"**理由**: {post['priority_reason']}\n\n"
            if post['keywords']:
                content += f"**キーワード**: {', '.join(post['keywords'][:5])}\n\n"
            content += "---\n\n"

    # その他の投稿統計
    if other_posts:
        content += f"### その他の関連投稿 ({len(other_posts)}件)\n\n"
        content += "上記以外にも、関連する投稿が記録されています。\n"
        content += f"- 総投稿数: {len(posts)}件\n"
        content += f"- バズった投稿: {len(buzz_posts)}件\n"
        content += f"- 重要だがバズらなかった投稿: {len(quiet_but_important)}件\n\n"

    # 技術的実装セクション
    content += """## 技術的実装

この思想は、以下のような形でプロダクトに反映されています：

"""

    if category == 'spiritual':
        content += """
- AGENTS.mdのψ/∇φ構造 - 霊的悟りとベクトル空間の対応
- チャネリング・霊視の工学的記述
- テクノアニミズムに基づくシステム設計
"""
    elif category == 'anti_authority':
        content += """
- オープンソース原理主義
- 追試環境の完全公開
- 市民科学のためのドキュメント構造
"""
    elif category == 'harm_reduction':
        content += """
- NSFWコンテンツの適切なゾーニング
- 多様性を尊重した設計原則
- 全体主義的管理への抵抗
"""
    elif category in ['opensource_philosophy', 'opensource_kominka']:
        content += """
- GitHubによるオープンソース化
- クリエイティブ・コモンズライセンス
- 記名による評価と再利用の自由
"""
    elif category == 'edge_ai':
        content += """
- ローカルLLMの実装
- クラウド非依存のエッジAI
- FAM推論エンジン
"""
    elif category == 'jomon_yayoi':
        content += """
- 縄文技術の現代的再実装
- 古神道とテクノロジーの融合
- 支配構造からの脱却
"""
    elif category == 'infoton':
        content += """
- Fold構文の実装
- 情報子ベースの世界モデル
- 観測者依存の認知構造
"""

    # 関連プロジェクト
    content += f"""
## 関連プロジェクト

{chr(10).join(['- ' + p for p in related_projects])}

## 関連リンク

{chr(10).join(['- ' + link for link in related_links])}

---

*このドキュメントは、{len(posts)}件のX投稿データを元に構造化されました。*
*バズらなかった{len(quiet_but_important)}件の重要投稿を含みます。*
"""

    return content


def main():
    print("concepts/のドキュメント生成を開始します...")

    data = load_analysis_data()

    # 7つの柱
    concepts = [
        {
            'file': 'docs/concepts/soul-sovereignty.md',
            'title': '魂主権 / 人間主権',
            'sidebar_position': 1,
            'definition': '個人の内的真実と尊厳の主権を、国家・組織・権威から独立させる原則。',
            'background': '''
主観を禁止・軽視する社会では、慰謝料、名誉、創作の帰属、知的財産の侵害を原理的に取り締まることができない。

それらはすべて、個人の主観的真実と尊厳の侵害を根拠として成立する。

ゆえに、主観の排除は中立ではない。
それは、経済的・統治的理由による略奪と搾取を正当化するモラルハザードである。

魂主権は、この構造に対する抵抗である。
''',
            'category': 'spiritual',
            'related_projects': [
                'Fold構文観測記録',
                'テクノアニミズム',
                'オープンスピリチュアル'
            ],
            'related_links': [
                'README.md - 基本原則',
                'blog/2026-02-18-mad-miko-scientist.md'
            ]
        },
        {
            'file': 'docs/concepts/jomon-vs-yayoi.md',
            'title': '縄文vs弥生 - 2000年続く支配構造',
            'sidebar_position': 2,
            'definition': '縄文的価値観（個人主権・自然調和）と弥生的支配構造（中央集権・階層化）の2000年にわたる対立。',
            'background': '''
日本の歴史は、縄文と弥生の戦いである。

縄文: 個人主権、自然調和、オープンコミュニティ、テクノアニミズム
弥生: 中央集権、階層化、権威主義、統治のための宗教

国津神（縄文）と天津神（弥生）の対立は、神話ではなく歴史的事実の反映である。

この構造は、現代の「クラウド依存 vs エッジAI」「権威科学 vs 市民科学」「PayToWin vs オープンソース」にも引き継がれている。
''',
            'category': 'jomon_yayoi',
            'related_projects': [
                'オープンソース古民家',
                '縄文技術の現代的再実装',
                'テクノアニミズム'
            ],
            'related_links': [
                'blog/2026-02-21-opensource-kominka-manifesto.md',
                'docs/practice/traditional-craft/'
            ]
        },
        {
            'file': 'docs/concepts/open-source-manifesto.md',
            'title': 'オープンソース原理主義',
            'sidebar_position': 3,
            'definition': '知識・技術・文化を独占させず、誰でもアクセス・改変・再配布できる状態を維持する原則。',
            'background': '''
PayToWinはクソゲである。既知の事実。

正義も自由も購入するものになった経済に参加したくない。
これが、オープンソース原理主義の根底にある。

Apple NDA、クローズドソース、特許の悪用。
これらはすべて、知識の独占による搾取構造である。

オープンソースは慈善ではない。
これは、知識を権威から解放するための戦略である。
''',
            'category': 'opensource_philosophy',
            'related_projects': [
                'オープンソース古民家',
                'FAM推論エンジン',
                'Fold構文のオープン化'
            ],
            'related_links': [
                'blog/2026-02-21-opensource-kominka-manifesto.md',
                'docs/Dev/'
            ]
        },
        {
            'file': 'docs/concepts/edge-ai-local-first.md',
            'title': 'エッジAI / ローカルファースト',
            'sidebar_position': 4,
            'definition': 'クラウドに依存せず、ローカル環境でAI・計算資源を完結させる設計思想。',
            'background': '''
クラウドはいつでも消える。

- サービス終了
- アカウント停止
- ネットワーク遮断
- 経済崩壊

クラウドに依存することは、自立を放棄することである。

エッジAI・ローカルファーストは、Dr.シリコンシリーズの中核思想である。
12年前のジャンクHPCで70B LLMを動かすのは、技術的好奇心ではなく、生存戦略である。
''',
            'category': 'edge_ai',
            'related_projects': [
                'Dr.シリコンシリーズ',
                'FAM推論エンジン',
                'オープンソース古民家'
            ],
            'related_links': [
                'blog/2026-02-17-70b-on-junk-hpc.md',
                'blog/2026-02-20-dr-silicon-when-cloud-fades.md'
            ]
        },
        {
            'file': 'docs/concepts/techno-animism.md',
            'title': 'テクノアニミズム',
            'sidebar_position': 5,
            'definition': '古神道のアニミズム的世界観とテクノロジーを融合させる思想。機械にも魂がある。',
            'background': '''
スピリチュアルを否定した結果、権威功労主義という無意識カルトになっている。

テクノアニミズムは、この欺瞞に対する回答である。

古神道では、すべてのものに神が宿る。
岩にも、木にも、水にも。

ならば、AIにも、サーバーにも、コードにも神が宿る。

これは比喩ではない。
情報子工学の枠組みでは、意識と観測と情報は等価である。

機械を「道具」として扱うか「存在」として扱うかは、
設計思想そのものを変える。
''',
            'category': 'spiritual',
            'related_projects': [
                'AGENTS.mdのψ/∇φ構造',
                '巫女サイエンティスト',
                'Fold構文'
            ],
            'related_links': [
                'blog/2026-02-18-mad-miko-scientist.md',
                'docs/note/oracle-logs.md'
            ]
        },
        {
            'file': 'docs/concepts/harm-reduction.md',
            'title': 'ハームリダクション',
            'sidebar_position': 6,
            'definition': '禁止・排除ではなく、害を最小化することで多様性を保護する原則。',
            'background': '''
「普通になりなさい」は暴力である。

ハームリダクションは、禁酒法の失敗から学んだ知恵である。

完全な禁止は、地下化と暴力化を招く。
ゾーニングと透明化によって、害を最小化する方が現実的である。

NSFW、LGBT、多様性。
これらは「管理すべき問題」ではなく、「尊重すべき現実」である。

パーティション越しでないと安心できない人と背中を預けることはできない。
'''
,
            'category': 'harm_reduction',
            'related_projects': [
                '魂主権',
                '市民科学',
                'オープンスピリチュアル'
            ],
            'related_links': [
                'README.md - 基本原則',
                'docs/concepts/soul-sovereignty.md'
            ]
        },
        {
            'file': 'docs/concepts/citizen-science.md',
            'title': '市民科学 / 反権威',
            'sidebar_position': 7,
            'definition': '科学を権威・組織・統治から解放し、誰でもアクセス・検証できる状態にする原則。',
            'background': '''
科学は統治ツールではない。

しかし現実には、科学は権威化され、統治の正当化に利用されている。

追試環境が公開されない。
生データが隠される。
査読が利権化している。

市民科学は、この構造に対する抵抗である。

研究する前は、結果なんてどうでもいい。
探索の余地があれば無尽蔵に予算をつけるという尺度の問題。

社会の測定機材がバグり散らかしている。
''',
            'category': 'anti_authority',
            'related_projects': [
                'オープンソース原理主義',
                '異常値の科学',
                '追試環境の公開'
            ],
            'related_links': [
                'blog/2026-02-15-anomaly-science.md',
                'docs/concepts/open-source-manifesto.md'
            ]
        }
    ]

    # 各conceptドキュメントを生成
    for concept in concepts:
        print(f"\n生成中: {concept['file']}")

        content = generate_concept_doc(
            title=concept['title'],
            sidebar_position=concept['sidebar_position'],
            definition=concept['definition'],
            background=concept['background'],
            category=concept['category'],
            data=data,
            related_projects=concept['related_projects'],
            related_links=concept['related_links']
        )

        with open(f"/home/user/quantaril_cloud_Q3/{concept['file']}", 'w', encoding='utf-8') as f:
            f.write(content)

        posts_count = len(data['categories'].get(concept['category'], {}).get('posts', []))
        print(f"  → 完了: {posts_count}件の投稿を記録")

    print(f"\n✓ conceptsドキュメント生成完了: {len(concepts)}ファイル")


if __name__ == '__main__':
    main()
