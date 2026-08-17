import supplySource from '@site/data/patron/supply.json';
import styles from './styles.module.css';
import type {SupplyRecord} from './types';

const records = supplySource.records as SupplyRecord[];

const statusLabels: Record<SupplyRecord['status'], string> = {
  UNKNOWN: '未観測',
  DORMANT: '休眠 / 再起動待ち',
  LOW: '不足',
  STABLE: '安定',
  SURPLUS: '余力あり',
};

export default function SupplyHud() {
  return (
    <section className={styles.supplyGrid} aria-label="Supply Level">
      {records.map((record) => (
        <article className={styles.supplyCard} data-status={record.status} key={record.id}>
          <div className={styles.cardTopline}>
            <h2>{record.label}</h2>
            <span className={styles.status}>{record.status}</span>
          </div>
          <p>{statusLabels[record.status]}</p>
          <small>{record.updatedAt ? `観測: ${record.updatedAt}` : '観測時刻: UNKNOWN'}</small>
          {record.note ? <p className={styles.note}>{record.note}</p> : null}
        </article>
      ))}
    </section>
  );
}
