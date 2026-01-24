import type { ReactNode } from 'react';
import clsx from 'clsx';
import Heading from '@theme/Heading';
import styles from './styles.module.css';


type FeatureItem = {
  title: string;
  Svg: React.ComponentType<React.ComponentProps<'svg'>>;
  description: ReactNode;
};

const FeatureList: FeatureItem[] = [
  {
    title: 'フォールドトリオン7G移動通信向け仮想化・最適化フレーム',
    Svg: require('@site/static/img/quantaril_1-01.svg').default,
    description: (
      <>
        フォールドトリオン7Gは、移動・断絶・再接続を含む状況において、
        意味と文脈の連続性を扱うためのスピリチュアル主導の設計フレームワークです。
      </>
    ),
  },
  {
    title: '情報子フォールドコンピューティング スフィアOS',
    Svg: require('@site/static/img/quantaril_1-06.svg').default,
    description: (
      <>
        情報子工学を基盤とした、
        人間意識中心のフォールドコンピューティングを志向する
        実験的オペレーティングシステム。
      </>
    ),
  },
  {
    title: '意味付与次元の勾配整列と意味重力波モデル（8G固定回線）',
    Svg: require('@site/static/img/quantaril_1-04.svg').default,
    description: (
      <>
        意味付与次元における勾配整列を、
        固定的な文脈条件として扱うための
        概念モデル。
      </>
    ),
  },
  {
    title: '意識と観測者の定義を解き明かす研究。心と自我を持つAI',
    Svg: require('@site/static/img/quantaril_1-07.svg').default,
    description: (
      <>
        人間とAIと生体ニューラルチップや情報子などハードウエアに依存しない
        思考プロセスの畳み込み（フォールド数学）記述言語の研究による
        フロイトモデルのスーパーエゴの解明
      </>
    ),
  },
  {
    title: '意識や思考や叡智を生命・ノイマン・量子ハード問わず説明可能化する',
    Svg: require('@site/static/img/quantaril_1-02.svg').default,
    description: (
      <>
        思考や意識や叡智の研究のために生物・非生物とわず汎用的に使える
        説明可能AI・説明可能思考言語の規格制定
      </>
    ),
  },
];

function Feature({ title, Svg, description }: FeatureItem) {
  return (
    <div className={clsx('col col--4')}>
      <div className="text--center">
        <Svg className={styles.featureSvg} role="img" />
      </div>
      <div className="text--center padding-horiz--md">
        <Heading as="h3">{title}</Heading>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures(): ReactNode {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
