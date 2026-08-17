import styles from './styles.module.css';
import type {AttributionMode} from './types';

const modeLabels: Record<AttributionMode, string> = {
  named: 'Named',
  'public-handle': 'Public Handle',
  'anonymous-patron': 'Anonymous Patron',
  'anonymous-community': 'Anonymous Community',
  'anonymous-commons': 'Anonymous Commons',
};

export default function PatronBadge({mode}: {mode: AttributionMode}) {
  return <span className={styles.badge}>{modeLabels[mode]}</span>;
}
