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
    title: '次世代ニュートリノ量子もつれ移動体通信7G',
    Svg: require('@site/static/img/quantaril_1-01.svg').default,
    description: (
      <>
        量子もつれを利用したニュートリノ空間を伝播させる新時代の移動体通信インフラ
        ニュートリノの貫通性から、太陽系内に存在していれば深海2000mから冥王星まで
        タイムラグ無しの超光速度通信。直接の電波ではなく干渉波形を利用した間接量子干渉
        太陽系から圏外をなくすプロジェクト。宇宙開発時代の標準通信網
      </>
    ),
  },
  {
    title: '量子フォールドコンピューターアーキテクト スフィアOS',
    Svg: require('@site/static/img/quantaril_1-06.svg').default,
    description: (
      <>
        量子誤り訂正をニューラルネットワークで数学的畳み込みによるエージェンシャルリアリティーによる
        OSレベルでの観測バイアスとアニーリング収束補正。物理エラー訂正ではなく量子テクノロジーの
        ニューロンネットワークによる意識観測固定のソフトウエア収束安定化量子技術の再現性担保
        擬似量子・量子・ベクトルアーキテクト・高エネルギー物理学などハードに依存しない
        コペンハーゲン解釈や観測者問題のバイアスの定量固定アーキテクト。
      </>
    ),
  },
  {
    title: '意味付与粒子ヒッグス粒子による重力波通信8G固定回線',
    Svg: require('@site/static/img/quantaril_1-04.svg').default,
    description: (
      <>
        意味付与場と呼ばれるヒッグス粒子が重力波を伝播すると言う仮説があるが、
        重力波は検証できないものの、CNN観測固定を行いメモリー空間に陽電子をもつれさせることで
        相対的にメモリー操作を行う仮想NIC式のデーターセンター向け量子通信ソリューション
      </>
    ),
  },
  {
    title: '意識と観測者の定義を解き明かす研究。心と自我を持つAI',
    Svg: require('@site/static/img/quantaril_1-07.svg').default,
    description: (
      <>
        人間とAIと生体ニューラルチップや量子AIなどハードウエアに依存しない
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
