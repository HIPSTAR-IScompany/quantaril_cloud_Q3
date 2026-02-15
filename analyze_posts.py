#!/usr/bin/env python3
"""
X投稿データ（CSV）を分析し、可燃性の高いコンテンツを抽出するスクリプト

重要: バズった/バズらないは参考値に過ぎない。思想的重要性が最優先。
インプレッション数が低くても、可燃性や思想的コアに関わる投稿は必ず拾う。
"""

import csv
import json
import re
from collections import defaultdict
from datetime import datetime


# カテゴリ定義とキーワードマッピング
CATEGORY_KEYWORDS = {
    # 可燃性カテゴリ（優先度高）
    'spiritual': {
        'keywords': [
            'スピリチュアル', '霊', '巫女', '神', '降霊', 'チャネリング', 'テクノアニミズム',
            '信託', 'お告げ', '霊的', '悟り', '古神道', '神道', '国津神', '天津神',
            '霊視', 'アニミズム', '精霊', '魂'
        ],
        'priority_base': 100
    },
    'infoton': {
        'keywords': [
            '情報子', '量子', '観測者', '世界線', '意識', 'シミュレーション',
            'ψ', '∇φ', 'FAM', 'Fold', 'パラダイムシフト', '情報子工学'
        ],
        'priority_base': 100
    },
    'project_fapta': {
        'keywords': [
            'FIAT', 'Fiat', 'ファプタ', 'プロジェクトファプタ', 'サービス終了',
            '通貨崩壊', '構造暴力', 'ビットコイン', 'Bitcoin', 'BTC',
            'ハイパーインフレ', '経済崩壊', '米ドル', 'NASDAQ', '財布'
        ],
        'priority_base': 100
    },
    'anomaly': {
        'keywords': [
            '異常値', '外れ値', '統計', '科学的コンセンサス', '追試',
            '再現性', 'プラシーボ', 'ファクトチェック', '測定', '検証'
        ],
        'priority_base': 100
    },
    'nde': {
        'keywords': [
            '臨死体験', '幽体離脱', 'カルマ', '輪廻', '転生', '来世',
            '死後', 'あの世', 'この世'
        ],
        'priority_base': 100
    },
    'anti_authority': {
        'keywords': [
            '反権威', '市民科学', 'ハッキング', '合法化', '追試環境',
            '権威', '政府', '統治', 'オープンソース', '公開',
            '権威功労主義', 'カルト', '無意識'
        ],
        'priority_base': 100
    },
    'harm_reduction': {
        'keywords': [
            'NSFW', '多様性', 'LGBT', '禁酒法', '普通になりなさい',
            'ハームリダクション', '規制', '管理', '全体主義',
            'パーティション', '隔離', 'ゾーニング'
        ],
        'priority_base': 100
    },
    'jomon_yayoi': {
        'keywords': [
            '縄文', '弥生', '国津神', '天津神', '2000年',
            '支配構造', '戦い', '縄文技術'
        ],
        'priority_base': 100
    },

    # プロジェクトシリーズ
    'dr_silicon': {
        'keywords': [
            'Dr.シリコン', 'Drシリコン', 'When The Cloud Fades',
            'クラウドが消えた'
        ],
        'priority_base': 100
    },
    'opensource_kominka': {
        'keywords': [
            'オープンソース古民家', '古民家', 'Open Source Hardware Architecture',
            'OSHA', 'Japan', '古民家DIY'
        ],
        'priority_base': 100
    },
    'survival_diy': {
        'keywords': [
            'サバイバル', 'DIY', '極限生活', '自給自足',
            '焼畑', '農業', '生存'
        ],
        'priority_base': 80
    },

    # 技術カテゴリ
    'tech_achievement': {
        'keywords': [
            '70B', 'LLM', 'Hackintosh', 'CPU推論', '魔改造',
            'ハイパーバイザー', 'HPC', 'ジャンク', 'GPU',
            'メモリ帯域', 'スケジューリング', '仮想化'
        ],
        'priority_base': 80
    },
    'opensource_philosophy': {
        'keywords': [
            'オープンソース', 'OpenSource', 'PayToWin', 'Apple NDA',
            '寺子屋', 'クリエイティブ・コモンズ', 'CC', 'ライセンス',
            'GitHub', '記名', 'パクって', 'OKだよ'
        ],
        'priority_base': 90
    },
    'edge_ai': {
        'keywords': [
            'エッジAI', 'ローカルファースト', 'クラウド拒否',
            'FAM推論', 'ローカルLLM', 'エッジ'
        ],
        'priority_base': 80
    },

    # 生活知識カテゴリ
    'material_science': {
        'keywords': [
            '素材工学', '物性', 'ミネラル', 'ニガリ', '塩',
            'イオンチャンネル', 'Na', 'Mg', 'Cl', 'マイクロメーター',
            'ダイラタント', '非ニュートン', '片栗粉'
        ],
        'priority_base': 70
    },
    'traditional_craft': {
        'keywords': [
            '巫女装束', '古神道', '伝統工芸', '縄文技術',
            '岩塩', '塩公正取引委員会'
        ],
        'priority_base': 70
    },
}

# プロジェクトシリーズの判定
PROJECT_SERIES = {
    'dr_silicon': ['Dr.シリコン', 'Drシリコン', 'When The Cloud Fades'],
    'opensource_kominka': ['オープンソース古民家', '古民家', 'Open Source Hardware Architecture'],
    'project_fapta': ['FIAT', 'Fiat', 'ファプタ', 'プロジェクトファプタ']
}


def classify_post(text):
    """投稿を複数カテゴリに分類し、キーワードも抽出"""
    categories = []
    keywords_found = []

    for category, data in CATEGORY_KEYWORDS.items():
        for keyword in data['keywords']:
            if keyword.lower() in text.lower():
                if category not in categories:
                    categories.append(category)
                if keyword not in keywords_found:
                    keywords_found.append(keyword)

    return categories, keywords_found


def detect_project_series(text):
    """プロジェクトシリーズを検出"""
    for series_name, keywords in PROJECT_SERIES.items():
        for keyword in keywords:
            if keyword in text:
                return series_name
    return None


def calculate_priority(categories, impressions, engagement_rate, project_series):
    """
    優先度スコアを計算

    基準の優先順位:
    1. 思想的重要性: 7つの柱、可燃性宣言、プロジェクト固有の思想 → インプレッション数に関わらず全件抽出
    2. プロジェクトシリーズ: Dr.シリコン、オープンソース古民家、プロジェクトファプタ → 全件抽出
    3. バズ指標: インプレッション > 5,000 OR エンゲージメント率 > 5% → 参考として優先度を上げる
    """
    priority_score = 0
    reasons = []

    # 思想カテゴリに該当 → 自動的に優先度MAX
    thought_categories = [
        'spiritual', 'infoton', 'project_fapta', 'anomaly', 'nde',
        'anti_authority', 'harm_reduction', 'jomon_yayoi'
    ]

    for category in categories:
        if category in thought_categories:
            priority_score = max(priority_score, 100)
            reasons.append(f"思想的コア: {category}")
        elif category in CATEGORY_KEYWORDS:
            priority_score = max(priority_score, CATEGORY_KEYWORDS[category]['priority_base'])

    # プロジェクトシリーズに該当 → 優先度MAX
    if project_series:
        priority_score = max(priority_score, 100)
        reasons.append(f"プロジェクトシリーズ: {project_series}")

    # バズ指標は加点要素
    if impressions > 5000:
        priority_score += 20
        reasons.append(f"高インプレッション: {impressions}")

    if engagement_rate > 0.05:
        priority_score += 10
        reasons.append(f"高エンゲージメント率: {engagement_rate:.2%}")

    # 優先度50以上を全て抽出
    priority_reason = "; ".join(reasons) if reasons else "一般投稿"

    return priority_score, priority_reason


def recommend_destination(categories, project_series):
    """ドキュメントの推奨配置先を決定"""
    if project_series == 'dr_silicon':
        return "docs/projects/dr-silicon/intro.md"
    elif project_series == 'opensource_kominka':
        return "docs/projects/opensource-kominka/intro.md"
    elif project_series == 'project_fapta':
        return "docs/projects/project-fapta/intro.md"

    # カテゴリベースの推奨
    category_destinations = {
        'spiritual': 'docs/note/oracle-logs.md',
        'infoton': 'docs/Dev/infoton-engineering.md',
        'nde': 'docs/note/near-death.md',
        'anti_authority': 'docs/concepts/citizen-science.md',
        'harm_reduction': 'docs/concepts/harm-reduction.md',
        'jomon_yayoi': 'docs/concepts/jomon-vs-yayoi.md',
        'tech_achievement': 'blog/technical-achievements.md',
        'opensource_philosophy': 'docs/concepts/open-source-manifesto.md',
        'edge_ai': 'docs/concepts/edge-ai-local-first.md',
        'material_science': 'docs/practice/material-science/',
        'traditional_craft': 'docs/practice/traditional-craft/',
    }

    for category in categories:
        if category in category_destinations:
            return category_destinations[category]

    return "docs/general/"


def analyze_csv(csv_path):
    """CSVを分析し、カテゴリ分類と優先度付けを行う"""
    results = defaultdict(lambda: {'posts': []})
    stats = {
        'total_posts': 0,
        'extracted_by_thought': 0,
        'extracted_by_buzz': 0,
        'extracted_by_project': 0,
        'total_extracted': 0,
        'low_impression_but_important': 0
    }

    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)

        for row in reader:
            stats['total_posts'] += 1

            post_id = row['ポストID']
            date = row['日付']
            text = row['ポスト本文']
            link = row['ポストのリンク']

            # 空行をスキップ
            if not post_id or not text:
                continue

            try:
                impressions = int(row['インプレッション数']) if row['インプレッション数'] else 0
                likes = int(row['いいね']) if row['いいね'] else 0
                engagements = int(row['エンゲージメント']) if row['エンゲージメント'] else 0
            except ValueError:
                impressions = 0
                likes = 0
                engagements = 0

            # エンゲージメント率の計算
            engagement_rate = engagements / impressions if impressions > 0 else 0

            # カテゴリ分類
            categories, keywords = classify_post(text)

            # プロジェクトシリーズ検出
            project_series = detect_project_series(text)

            # 優先度計算
            priority_score, priority_reason = calculate_priority(
                categories, impressions, engagement_rate, project_series
            )

            # 優先度50以上を抽出
            if priority_score >= 50:
                post_data = {
                    'post_id': post_id,
                    'date': date,
                    'text': text,
                    'link': link,
                    'impressions': impressions,
                    'likes': likes,
                    'engagements': engagements,
                    'engagement_rate': round(engagement_rate, 4),
                    'priority_score': priority_score,
                    'priority_reason': priority_reason,
                    'keywords': keywords,
                    'project_series': project_series,
                    'recommended_destination': recommend_destination(categories, project_series)
                }

                # 各カテゴリに追加
                if categories:
                    for category in categories:
                        results[category]['posts'].append(post_data)
                else:
                    results['uncategorized']['posts'].append(post_data)

                stats['total_extracted'] += 1

                # 統計更新
                if priority_score >= 100 and not ('高インプレッション' in priority_reason):
                    if '思想的コア' in priority_reason:
                        stats['extracted_by_thought'] += 1
                    if 'プロジェクトシリーズ' in priority_reason:
                        stats['extracted_by_project'] += 1

                if impressions > 5000 or engagement_rate > 0.05:
                    stats['extracted_by_buzz'] += 1

                # 低インプレッションだが重要な投稿
                if impressions < 1000 and priority_score >= 100:
                    stats['low_impression_but_important'] += 1

    # 各カテゴリ内で優先度順にソート
    for category in results:
        results[category]['posts'].sort(key=lambda x: (-x['priority_score'], -x['impressions']))

    return dict(results), stats


def main():
    csv_path = '/home/user/quantaril_cloud_Q3/src/Post/K_chachamaru/account_analytics_content_2025-11-16_2026-02-13.csv'
    output_path = '/home/user/quantaril_cloud_Q3/analysis_output.json'

    print("CSV分析を開始します...")
    results, stats = analyze_csv(csv_path)

    # 出力データの構造化
    output = {
        'extraction_stats': stats,
        'categories': results,
        'metadata': {
            'analyzed_at': datetime.now().isoformat(),
            'source_file': csv_path,
            'extraction_policy': '思想的重要性優先 - バズは参考値'
        }
    }

    # JSON出力
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"\n分析完了!")
    print(f"出力ファイル: {output_path}")
    print(f"\n=== 抽出統計 ===")
    print(f"総投稿数: {stats['total_posts']}")
    print(f"抽出された投稿: {stats['total_extracted']}")
    print(f"  - 思想的重要性による抽出: {stats['extracted_by_thought']}")
    print(f"  - プロジェクトシリーズによる抽出: {stats['extracted_by_project']}")
    print(f"  - バズ指標による抽出: {stats['extracted_by_buzz']}")
    print(f"  - バズらなかったが重要な投稿: {stats['low_impression_but_important']}")
    print(f"\n=== カテゴリ別投稿数 ===")
    for category, data in sorted(results.items(), key=lambda x: len(x[1]['posts']), reverse=True):
        print(f"{category}: {len(data['posts'])}件")


if __name__ == '__main__':
    main()
