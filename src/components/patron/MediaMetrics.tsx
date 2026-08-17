import mediaSource from '@site/data/patron/media.json';
import styles from './styles.module.css';
import type {MediaRecord} from './types';

const records = mediaSource.records as MediaRecord[];

export default function MediaMetrics() {
  if (records.length === 0) {
    return (
      <section className={styles.emptyState}>
        <h2>公開条件を満たす媒体観測値はまだありません</h2>
        <p>metric、period、observedAt、sourceRefが揃う値だけを掲載します。過去の表示回数を将来の最低保証にはしません。</p>
      </section>
    );
  }

  return (
    <section className={styles.metricGrid}>
      {records.map((record) => (
        <article className={styles.metricCard} key={record.id}>
          <p className={styles.kicker}>{record.platform}</p>
          <strong>{record.value.toLocaleString('ja-JP')}</strong>
          <h2>{record.metric}</h2>
          <p>{record.notes}</p>
          <small>観測: {record.observedAt}</small>
        </article>
      ))}
    </section>
  );
}
