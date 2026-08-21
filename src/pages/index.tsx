import type {ReactNode} from 'react';
import Head from '@docusaurus/Head';
import Link from '@docusaurus/Link';
import Layout from '@theme/Layout';
import Heading from '@theme/Heading';
import HomepageFeatures from '@site/src/components/HomepageFeatures';
import PayPalHostedButton from '@site/src/components/PayPalHostedButton';
import styles from './index.module.css';

const capabilityRows = [
  ['Sphere-DOS 開発シェル', '利用可能', 'ready'],
  ['複数AI作業面', '利用可能', 'ready'],
  ['試験用の判断核', '自動試験済み', 'ready'],
  ['コックピットGUI', 'レンダー試験済み', 'ready'],
  ['製品版ランナー', '未実装', 'pending'],
] as const;

const productPillars = [
  {
    code: 'WORLD',
    title: '世界を生やす',
    body: '神話、ゲーム、研究、組織ごとに、意味Kernelと因果と権限を持つWorldをつくる。違うWorldは混ぜず、Portalで対話させる。',
    status: 'SPEC / REFORGING',
  },
  {
    code: 'ASTRO',
    title: '個体と来歴を運ぶ',
    body: '人格、記憶、装備、関係、来歴を可搬な候補へ。copyを同一性と呼ばず、分岐、欠損、同意、writeback境界を残す。',
    status: 'SPEC / DESIGN',
  },
  {
    code: 'PORTAL',
    title: '現実へ門を開く',
    body: '既存OS、database、IAM、API、機器を置き換えず、必要なcapabilityだけをAtlantis Worldへ接続する。',
    status: 'OPEN / REVIEW-WANTED',
  },
] as const;

function HomepageHeader() {
  return (
    <header className={styles.heroBanner}>
      <div className={styles.heroBackdrop} aria-hidden="true" />
      <div className={`container ${styles.heroGrid}`}>
        <div className={styles.heroCopy}>
          <p className={styles.kicker}>SPHEREOS ATLANTIS · OPEN REFORGE</p>
          <Heading as="h1" className={styles.heroTitle}>
            いくつもの世界を生やし、<br />隔離し、橋を架けるためのOS。
          </Heading>
          <p className={styles.heroLead}>
            神話、人格、体験、技術を、一つの正しさへ潰さず次の器へ運ぶ。
            日本語を正本に、各言語へPortalを開く公開鍛造所です。
          </p>
          <div className={styles.heroActions}>
            <Link className={styles.primaryAction} to="/about/intro">この世界へ入る</Link>
            <Link className={styles.secondaryAction} to="/docs/intro">文書庫をひらく</Link>
            <a className={styles.ghostAction} href="https://github.com/HIPSTAR-IScompany/quantaril_cloud_QAtlantis">GitHub</a>
          </div>
          <p className={styles.heroFreedom}>感じる自由。信じる自由。疑う自由。語る自由。遊ぶ自由。フォークする自由。</p>
        </div>

        <aside className={styles.consolePanel} aria-label="Q Atlantis 開発入口">
          <div className={styles.consoleTopbar}>
            <span className={styles.consoleLights}><i /><i /><i /></span>
            <span>Sphere-DOS / Prompt Engineering</span>
            <span>0.250.1</span>
          </div>
          <div className={styles.consoleBody}>
            <p><span className={styles.prompt}>atlas@forge:~$</span> /man</p>
            <p className={styles.consoleLabel}>利用できる入口</p>
            <nav className={styles.consoleNav}>
              <Link to="/about/intro"><b>[1]</b><span>世界を見渡す<small>思想・神話・研究・現在地</small></span></Link>
              <a href="https://codespaces.new/HIPSTAR-IScompany/quantaril_cloud_QAtlantis"><b>[2]</b><span>Codespacesで起動<small>リポジトリ接続済み開発環境</small></span></a>
              <Link to="/docs/engineering/q-atlantis/"><b>[3]</b><span>Codex PLIから入る<small>マニフェストを読む共同開発入口</small></span></Link>
              <Link to="/docs/engineering/q-atlantis/status"><b>[4]</b><span>現在能力を検査する<small>実装・仕様・研究・資源待ち</small></span></Link>
            </nav>
            <div className={styles.capabilityTable}>
              {capabilityRows.map(([name, value, state]) => (
                <div key={name}><span>{name}</span><strong data-state={state}>{value}</strong></div>
              ))}
            </div>
            <p className={styles.consoleLabel}>試験用部品が動くことと、完成品として配れることは別です。</p>
          </div>
        </aside>
      </div>
      <p className={styles.developmentNote}>※開発中の画面です。実際の製品・実装状態とは異なる場合があります。</p>
    </header>
  );
}

function ProductVision() {
  return (
    <section className={styles.productVision}>
      <div className="container">
        <div className={styles.visionHeader}>
          <p className={styles.eyebrow}>虚構プロトタイプから、触れる公開鍛造所へ</p>
          <Heading as="h2">世界を描画する道具から、世界を動かす道具へ。</Heading>
          <p>創作上の「虚空の揺籠」から始まったロマン砲を、神話は神話のまま、工学は検証可能なcomponentとしてQ Atlantisへ鍛造しています。</p>
        </div>
        <div className={styles.pillarGrid}>
          {productPillars.map((pillar, index) => (
            <article className={styles.pillarCard} key={pillar.code}>
              <div className={styles.pillarMeta}><span>0{index + 1}</span><b>{pillar.code}</b></div>
              <Heading as="h3">{pillar.title}</Heading>
              <p>{pillar.body}</p>
              <small>{pillar.status}</small>
            </article>
          ))}
        </div>
        <div className={styles.visionLinks}>
          <Link className={styles.primaryAction} to="/about/vision">プロダクトビジョン</Link>
          <Link className={styles.secondaryAction} to="/docs/engineering/q-atlantis/product-line">製品系列と現在能力</Link>
        </div>
      </div>
    </section>
  );
}

function ForgeSupport() {
  return (
    <section id="support" className={styles.forgeSupport} aria-labelledby="support-title">
      <div className={`container ${styles.supportGrid}`}>
        <div>
          <p className={styles.eyebrow}>JOMON 2.0 · OKITAMA CULTURAL COMMONS</p>
          <Heading as="h2" id="support-title">一匹の妖怪ではなく、陸奥御伽街道の生態系へ。</Heading>
          <p>
            「縄文2.0」は、誰か一人の成功へ資源を集中する計画ではなく、異なる世界観、人、技術、信仰、芸術が枯れずに共存できる文化圏を残すための活動です。
            齋藤みつるやQ Atlantisも、その生態系に棲む妖怪の一部にすぎません。
          </p>
          <p>
            この窓口からの支援は、個人のオカルトマイニングやQ Atlantis単体への直接投資ではありません。
            置賜郡射程の文化保護NPOと地域活動へ入り、文化、福祉、交通、設備、広報、町おこしなど、その時点で必要と判断された場所へ非線形に巡ります。
            配分の優先度は地域側の事情によって変わり、作者個人が指定・管理するものではありません。
          </p>
          <p>
            そのため、特定の寄付が特定の成果へ直結すること、齋藤みつる本人へ届くこと、個別案件の詳細な因果や会計説明を作者が保証することはできません。
            支援は「この一人を救う」よりも、陸奥御伽街道の妖怪、文化、実験、語りがまとめて絶滅しないための町おこしとして受け取ってください。
          </p>
          <p>
            お金だけが参加方法ではありません。拡散、翻訳、技術協力、記録、現物、地域との橋渡しも、文化圏を維持する同じ贈与回路です。
          </p>
          <p>
            齋藤みつる本人を直接応援したい、あるいは妖怪へ餌付けしたい場合は、
            <a href="https://x.com/K_chachamaru">X（@K_chachamaru）</a>のDMで相談してください。
            ギフト券、物理直送、生もふもふりなどを受け取れる場合があります。
            ただしXのアンチスパム・詐欺対策によって、突然届いたギフト券コードが見えない場所へ入ることがあります。
            支援する側から先に公開メンションで「DMでAmazonギフトを送った」「物を送りたい」など贈与意思を知らせ、その後にDMを送ってください。
            齋藤みつる側から個別にギフト券を要求する運用はしません。ギフト券コードや住所などの秘密情報は、公開メンションへ書かずDMだけで扱ってください。
          </p>
        </div>
        <div className={styles.supportPanel}>
          <div className={styles.supportPanelInner}>
            <PayPalHostedButton hostedButtonId="6LVN8W5RS77NU" className={styles.paypalFrame} />
            <p className={styles.supportPolicy}>
              このフォームはQ Atlantis単体の持分販売や直接投資ではありません。
              支援の前に、<Link to="/about/stewardship">非独占方針・芳名台帳・資金の行き先</Link>を確認できます。
            </p>
          </div>
        </div>
      </div>
    </section>
  );
}

export default function Home(): ReactNode {
  const pageTitle = '神話・人格・技術を運ぶ公開鍛造所';
  const pageDescription = 'Q Atlantisは、神話・人格・体験・技術を一つの正しさへ潰さず、World・Fold・OAEとして運ぶ公開研究鍛造所です。';

  return (
    <Layout title={pageTitle} description={pageDescription}>
      <Head>
        <meta name="keywords" content="Q Atlantis, SphereOS, 情報子工学, 意味資源OS, Fold, OAE, Gaming Cosmology, オープンサイエンス, OSS" />
        <meta property="og:type" content="website" />
        <meta property="og:site_name" content="Q Atlantis" />
        <meta property="og:title" content={`${pageTitle} · Q Atlantis`} />
        <meta property="og:image:alt" content="複数のWorldをPortalでつなぐQ Atlantis公開鍛造所" />
        <meta name="twitter:title" content={`${pageTitle} · Q Atlantis`} />
        <meta name="twitter:description" content={pageDescription} />
        <meta name="twitter:image:alt" content="複数のWorldをPortalでつなぐQ Atlantis公開鍛造所" />
      </Head>
      <div className={styles.homeShell}>
        <HomepageHeader />
        <main>
          <ProductVision />
          <HomepageFeatures />
          <ForgeSupport />
        </main>
      </div>
    </Layout>
  );
}
