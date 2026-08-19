import Link from '@docusaurus/Link';
import offeringsSource from '@site/data/patron/offerings.json';
import serviceSource from '@site/data/patron/service.json';
import styles from './styles.module.css';
import type {PatronOffering, PatronService} from './types';

const service = serviceSource as PatronService;
const offerings = offeringsSource.records as PatronOffering[];

function yen(value: number) {
  return `${value.toLocaleString('ja-JP')}円`;
}

function termLabel(offering: PatronOffering) {
  if (offering.term.status === 'ADJUSTING') return '掲載期間を調整中';
  if (offering.term.mode === 'FIXED_HALF_YEAR') return '上半期／下半期の6か月cycle';
  return '公開開始日から起算';
}

export default function PatronServiceStatus() {
  const dmRoute = service.contact.routes.find((route) => route.kind === 'x-dm');

  return (
    <section className={styles.servicePanel} aria-labelledby="patron-service-status-title">
      <div className={styles.serviceHeader}>
        <div>
          <p className={styles.kicker}>PATRON SERVICE / {service.status}</p>
          <h2 id="patron-service-status-title">{service.statusLabel}</h2>
        </div>
        <span className={styles.status}>申込・決済は準備中</span>
      </div>

      <p>
        現在は相談のみ受け付けています。相談しても契約、予約、受付順、支払義務は発生しません。
      </p>

      <div className={styles.offeringGrid}>
        {offerings.map((offering) => (
          <article className={styles.offeringCard} key={offering.id}>
            <p className={styles.kicker}>{offering.availability}</p>
            <h3>{offering.label}</h3>
            <p className={styles.price}>{yen(offering.priceTaxIncludedJpy)}<small>／1口・税込</small></p>
            <p>税抜 {yen(offering.priceTaxExcludedJpy)}・口数上限なし</p>
            <p>{termLabel(offering)}</p>
            {offering.specStatus === 'ADJUSTING' ? <p className={styles.adjusting}>銘板仕様・物理枠数を調整中</p> : null}
          </article>
        ))}
      </div>

      <div className={styles.serviceActions}>
        {dmRoute ? <Link className="button button--primary" href={dmRoute.url}>開始前にDMで相談</Link> : null}
        <Link className="button button--secondary" to="/patron/policy/commercial-transactions">開始前の取引表示を確認</Link>
      </div>
    </section>
  );
}
