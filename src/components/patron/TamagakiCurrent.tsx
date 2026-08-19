import tamagakiSource from '@site/data/patron/tamagaki.json';
import styles from './styles.module.css';
import type {TamagakiRecord} from './types';

const records = [...(tamagakiSource.records as TamagakiRecord[])].sort((left, right) => {
  const cycleOrder = right.cycle.localeCompare(left.cycle);
  return cycleOrder === 0 ? left.acceptedSequence - right.acceptedSequence : cycleOrder;
});

export default function TamagakiCurrent({view = 'current'}: {view?: 'current' | 'archive'}) {
  const selected = records.filter((record) =>
    view === 'current'
      ? record.status === 'ACTIVE' || record.status === 'SCHEDULED'
      : record.status === 'RETIRED' || record.status === 'CANCELLED',
  );

  if (selected.length === 0) {
    return (
      <section className={styles.emptyState}>
        <h2>{view === 'current' ? '現在建立中の玉垣はありません' : '公開済みの退役記録はありません'}</h2>
        <p>申込、契約、支払、logo利用許諾が確定するまで架空の協賛枠を表示しません。</p>
      </section>
    );
  }

  return (
    <section className={styles.tamagakiGrid}>
      {selected.map((record) => (
        <article className={styles.tamagakiCard} key={record.id}>
          <p className={styles.kicker}>協賛広告 / {record.cycle}</p>
          <h2>{record.label}</h2>
          <p>{record.termStartsAt} — {record.termEndsAt}</p>
          <p>受付順 {record.acceptedSequence}</p>
          <span className={styles.status}>{record.status}</span>
        </article>
      ))}
    </section>
  );
}
