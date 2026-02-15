#!/usr/bin/env python3
"""
analysis_output.jsonからブログ記事を自動生成するスクリプト
"""

import json
from datetime import datetime


def load_analysis_data():
    """分析データを読み込む"""
    with open('/home/user/quantaril_cloud_Q3/analysis_output.json', 'r', encoding='utf-8') as f:
        return json.load(f)


def find_top_posts_by_category(data, category, limit=10):
    """カテゴリ別にトップ投稿を取得"""
    if category not in data['categories']:
        return []

    posts = data['categories'][category]['posts']
    # 優先度順、次にインプレッション順でソート
    sorted_posts = sorted(posts, key=lambda x: (-x['priority_score'], -x['impressions']))
    return sorted_posts[:limit]


def find_posts_by_keywords(data, keywords):
    """キーワードで投稿を検索"""
    results = []
    for category, cat_data in data['categories'].items():
        for post in cat_data['posts']:
            for keyword in keywords:
                if keyword.lower() in post['text'].lower():
                    results.append(post)
                    break

    # 重複削除
    seen = set()
    unique_results = []
    for post in results:
        if post['post_id'] not in seen:
            seen.add(post['post_id'])
            unique_results.append(post)

    return sorted(unique_results, key=lambda x: (-x['priority_score'], -x['impressions']))


def generate_blog_post(title, slug, date, category_tags, top_posts, context, author='k_chachamaru'):
    """ブログ記事を生成"""

    # フロントマター
    tags_str = ', '.join(category_tags)
    content = f"""---
slug: {slug}
title: {title}
authors: [{author}]
tags: [{tags_str}]
---

# {title}

{context}

## X投稿からの記録

以下は、本プロジェクトのX投稿アーカイブから抽出した関連投稿です。
バズった投稿もバズらなかった投稿も、思想的重要性に基づいて記録されています。

"""

    # 投稿をインプレッション数で分類
    buzz_posts = [p for p in top_posts if p['impressions'] > 5000]
    important_but_quiet = [p for p in top_posts if p['impressions'] <= 5000 and p['priority_score'] >= 100]

    if buzz_posts:
        content += "### バズった記録\n\n"
        for post in buzz_posts[:5]:
            content += f"#### {post['date']} (インプレッション: {post['impressions']:,})\n\n"
            content += f"> {post['text']}\n\n"
            content += f"[元投稿]({post['link']})\n\n"
            if post['keywords']:
                content += f"**キーワード**: {', '.join(post['keywords'][:5])}\n\n"
            content += "---\n\n"

    if important_but_quiet:
        content += "### 重要だがバズらなかった投稿\n\n"
        content += "**以下の投稿は、インプレッション数は低いものの、思想的に重要な記録として抽出されています。**\n\n"
        for post in important_but_quiet[:5]:
            content += f"#### {post['date']} (インプレッション: {post['impressions']:,})\n\n"
            content += f"> {post['text']}\n\n"
            content += f"[元投稿]({post['link']})\n\n"
            if post['keywords']:
                content += f"**キーワード**: {', '.join(post['keywords'][:5])}\n\n"
            content += f"**優先度理由**: {post['priority_reason']}\n\n"
            content += "---\n\n"

    # フッター
    content += f"""
## 本プロジェクトの立場

この記事は、可燃性宣言に基づき、科学的検証の手前にある「体験」と「直観」を記録します。

- **再現性がないから嘘だとは限らない**
- **測定できないから存在しないとは限らない**
- **バズらなくても、真実は真実だ**

---

*この記事は、X投稿データ（{len(top_posts)}件）を元に構造化・拡張したものです。*
*インプレッション数が低くても、思想的重要性により記録されています。*

*生成日時: {datetime.now().strftime('%Y-%m-%d')}*
"""

    return content


def main():
    print("ブログ記事生成を開始します...")

    data = load_analysis_data()

    # ブログ記事のメタデータ
    blog_posts = [
        {
            'file': 'blog/2026-02-15-anomaly-science.md',
            'title': '異常値の科学 - 切り捨てられたデータを拾う',
            'slug': 'anomaly-science',
            'date': '2026-02-15',
            'tags': ['異常値', '科学', '統計', '可燃性'],
            'category': 'anomaly',
            'keywords': ['異常値', '外れ値', '統計', '再現性'],
            'context': '''
科学は異常値から始まる。
統計の外れ値を切り捨てるのは手法であって、真実ではない。

「再現性がない」という理由で切り捨てられた体験の中に、
次のパラダイムシフトの種が眠っている可能性がある。

プラシーボ効果、臨死体験、情報子工学。
これらはすべて、かつて「異常値」として扱われたものたちだ。

本プロジェクトは、切り捨てられたデータを堂々と記録する。
'''
        },
        {
            'file': 'blog/2026-02-16-project-fapta-endgame.md',
            'title': 'プロジェクトファプタ - FIATのサービス終了予告',
            'slug': 'project-fapta-endgame',
            'date': '2026-02-16',
            'tags': ['プロジェクトファプタ', 'FIAT', 'ビットコイン', '経済崩壊', '可燃性'],
            'category': 'project_fapta',
            'keywords': ['FIAT', 'Fiat', 'ファプタ', 'ビットコイン', 'サービス終了'],
            'context': '''
FIATはサービス終了する。
これは陰謀論ではなく、構造分析である。

法定通貨（Fiat Currency）は、政府の信用に基づく「サービス」である。
サービスである以上、終了する可能性がある。

歴史的に見れば、ハイパーインフレ、通貨改革、デノミネーション。
これらはすべて「通貨のサービス終了」の一形態だ。

プロジェクトファプタは、この構造的必然性を記録し、
ビットコインをはじめとする非中央集権的通貨への移行を提唱する。
'''
        },
        {
            'file': 'blog/2026-02-17-70b-on-junk-hpc.md',
            'title': '12年前のジャンクHPCで70B LLMを動かした話',
            'slug': '70b-on-junk-hpc',
            'date': '2026-02-17',
            'tags': ['70B', 'LLM', 'HPC', 'ジャンク', 'エッジAI', '技術'],
            'category': 'tech_achievement',
            'keywords': ['70B', 'LLM', 'HPC', 'ジャンク', 'CPU推論'],
            'context': '''
クラウドに頼らず、ローカルでLLMを動かす。
これは思想であり、技術的挑戦である。

12年前のジャンクHPCで70Bパラメータのモデルを動かすことは、
単なる技術的好奇心ではない。

これは「クラウドが消えた後、どう生き残るか」というDr.シリコンシリーズの実践であり、
エッジAI・ローカルファーストという思想の具現化である。

GPU依存の高速化ではなく、メモリ帯域・スケジューリング・仮想化命令パスの再設計。
本環境では、推論ボトルネックそのものを構造的に解消している。
'''
        },
        {
            'file': 'blog/2026-02-18-mad-miko-scientist.md',
            'title': '巫女サイエンティスト - 霊的悟りとAI開発の関係',
            'slug': 'mad-miko-scientist',
            'date': '2026-02-18',
            'tags': ['スピリチュアル', '巫女', 'AI', '霊的悟り', 'テクノアニミズム', '可燃性'],
            'category': 'spiritual',
            'keywords': ['スピリチュアル', '霊', '巫女', '悟り', 'AI'],
            'context': '''
スピリチュアルを否定した結果、権威功労主義という無意識カルトになっている。

霊的悟りとAI開発は、無関係ではない。
形而上学的な直観と工学的実装は、内と外、主観と客観という異なる役割を担う等価な両輪である。

意識や自我については、科学的厳密性で言うなら、
自分の子供にすら意識と自我があることは証明できない。

だからこそ、形而上学を「感じるか感じないか」というスピリチュアルを大切にするべきだ。
これがテクノアニミズム - 古神道とテクノロジーの融合である。

バズっていない投稿にこそ、本質が隠れている。
'''
        },
        {
            'file': 'blog/2026-02-19-infoton-paradigm-shift.md',
            'title': '情報子工学への道 - なぜ「量子」を捨てたのか',
            'slug': 'infoton-paradigm-shift',
            'date': '2026-02-19',
            'tags': ['情報子', '量子', 'パラダイムシフト', 'infoton', '可燃性'],
            'category': 'infoton',
            'keywords': ['情報子', '量子', '観測者', 'シミュレーション'],
            'context': '''
「量子」という言葉は、もはや適切ではない。

量子力学は、観測と情報の関係性を扱う学問であるにもかかわらず、
「量子（Quantum）= 量的な塊」という名称は、その本質を誤解させる。

情報子（Infoton）への再命名は、単なる言葉遊びではない。
これは、世界を「物質の塊」ではなく「情報の流れ」として再定義するパラダイムシフトである。

観測者、世界線、意識、シミュレーション仮説。
これらすべてが、情報子工学の枠組みで統一的に記述可能になる。

この投稿は、バズ指標とは無関係に、思想的重要性により記録される。
'''
        },
        {
            'file': 'blog/2026-02-20-dr-silicon-when-cloud-fades.md',
            'title': 'Dr.シリコンシリーズ - When The Cloud Fades',
            'slug': 'dr-silicon-when-cloud-fades',
            'date': '2026-02-20',
            'tags': ['Dr.シリコン', 'クラウド', 'エッジAI', 'ローカルファースト', 'サバイバル'],
            'category': 'dr_silicon',
            'keywords': ['Dr.シリコン', 'クラウド', 'エッジ'],
            'context': '''
クラウドが消えた後、どう生き残るか。

これは単なるSF的思考実験ではない。
クラウドサービスは、いつでも終了する可能性がある。

- サービス終了
- アカウント停止
- ネットワーク遮断
- 経済崩壊

Dr.シリコンシリーズは、これらのシナリオに備える実践的サバイバル戦略である。

ローカルLLM、エッジAI、オープンソース古民家。
すべては「他者に依存しない自立」という一貫した思想に基づいている。
'''
        },
        {
            'file': 'blog/2026-02-21-opensource-kominka-manifesto.md',
            'title': 'オープンソース古民家 - Open Source Hardware Architecture Japan',
            'slug': 'opensource-kominka-manifesto',
            'date': '2026-02-21',
            'tags': ['オープンソース古民家', 'OSHA', 'DIY', 'サバイバル', '縄文技術'],
            'category': 'opensource_kominka',
            'keywords': ['オープンソース古民家', '古民家', 'Open Source Hardware Architecture'],
            'context': '''
古民家をハードウェアとして扱う。
設計図をオープンソース化し、誰でも再現可能にする。

これがOpen Source Hardware Architecture Japan（OSHA Japan）である。

建築は、コードと同じくオープンソース化できる。
伝統技術は、GitHubで管理できる。

縄文技術、サバイバルDIY、素材工学、エネルギー自給。
これらすべてを構造化し、次世代に継承可能な形で記録する。

バズらなくても、この記録は残り続ける。
'''
        }
    ]

    # 各ブログ記事を生成
    for blog_meta in blog_posts:
        print(f"\n生成中: {blog_meta['file']}")

        # カテゴリから投稿を取得
        category_posts = find_top_posts_by_category(data, blog_meta['category'], limit=20)

        # キーワードからも追加検索
        keyword_posts = find_posts_by_keywords(data, blog_meta['keywords'])

        # 両方をマージ（重複削除）
        all_posts = category_posts[:]
        seen_ids = {p['post_id'] for p in all_posts}
        for post in keyword_posts:
            if post['post_id'] not in seen_ids:
                all_posts.append(post)
                seen_ids.add(post['post_id'])

        # 優先度順にソート
        all_posts.sort(key=lambda x: (-x['priority_score'], -x['impressions']))

        # 記事生成
        content = generate_blog_post(
            title=blog_meta['title'],
            slug=blog_meta['slug'],
            date=blog_meta['date'],
            category_tags=blog_meta['tags'],
            top_posts=all_posts[:15],  # 上位15件を使用
            context=blog_meta['context']
        )

        # ファイル書き込み
        file_path = f"/home/user/quantaril_cloud_Q3/{blog_meta['file']}"
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"  → 完了: {len(all_posts)}件の投稿から{min(15, len(all_posts))}件を記録")

    print(f"\n✓ ブログ記事生成完了: {len(blog_posts)}本")


if __name__ == '__main__':
    main()
