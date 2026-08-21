import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

/**
 * Q Atlantis の公開文書は、ファイル名の偶然ではなく読者の目的で並べる。
 * 原典（sources）と旧生成器（pipeline）は Docusaurus の外に置く。
 */
const sidebars: SidebarsConfig = {
  projectSidebar: [
    'start/intro',
    {
      type: 'category',
      label: '読者・参加者別の入口',
      link: {type: 'doc', id: 'start/entrances/index'},
      items: [
        'start/entrances/spiritual-practitioner',
        'start/entrances/theologian',
        'start/entrances/philosopher',
        'start/entrances/gamer-playtester',
        'start/entrances/engineer',
        'start/entrances/infoton-engineer',
      ],
    },
    {
      type: 'category',
      label: '神話・世界観',
      link: {type: 'doc', id: 'worlds/index'},
      items: [
        {
          type: 'category',
          label: 'シミュレーション宇宙論',
          link: {type: 'doc', id: 'worlds/simulation-cosmology/intro'},
          items: [
            'worlds/simulation-cosmology/host',
            'worlds/simulation-cosmology/business',
          ],
        },
        'worlds/mythology/logos-structure',
        {
          type: 'category',
          label: '神学・信仰World',
          link: {type: 'doc', id: 'worlds/theology/index'},
          items: [
            'worlds/theology/divine-agency-and-host-ontology',
            'worlds/theology/responsibility-faith-sdk',
            'worlds/theology/scope-reconciliation-and-handoff',
            'worlds/theology/quantum-structural-theology',
          ],
        },
        'worlds/gaming/playtest-fairness-and-human-loop',
        'worlds/gaming/world-optimizer-fold',
      ],
    },
    {
      type: 'category',
      label: '体験・信仰・実践',
      link: {type: 'doc', id: 'practice/index'},
      items: [
        'practice/provisional-meaning-bridge',
        'practice/aim-diffusion-field',
        'practice/oracle/oracle-logs',
        'practice/channeling/channeling-engineering',
        'practice/experience-records/near-death',
        'practice/survival/index',
        'practice/traditional-craft/index',
        'practice/material-science/index',
      ],
    },
    {
      type: 'category',
      label: '哲学・思想',
      link: {type: 'doc', id: 'philosophy/index'},
      items: [
        'philosophy/soul-sovereignty',
        'philosophy/techno-animism',
        'philosophy/harm-reduction',
        'philosophy/human-is-loop-and-scope-non-monopoly',
        'philosophy/permission-spectrum-and-distributed-agency',
        'philosophy/open-source-manifesto',
        'philosophy/jomon-2.0-japan-gestalt-and-uzume',
        'philosophy/civilization/jomon-vs-yayoi',
      ],
    },
    {
      type: 'category',
      label: 'オカルト燃料庫',
      link: {type: 'doc', id: 'fuel/index'},
      items: [],
    },
    {
      type: 'category',
      label: '研究・仮説',
      link: {type: 'doc', id: 'research/index'},
      items: [
        'research/citizen-science',
        'research/infoton/quantum-to-infoton',
        'research/infoton/spiritual-dimension-and-oae',
        'research/infoton/infoton-engineering',
        'research/ai-llm/apple-illusion-of-thinking.ja',
        'research/ai-llm/apple-illusion-of-thinking.en',
      ],
    },
    {
      type: 'category',
      label: '工学・Q Atlantis',
      link: {type: 'doc', id: 'engineering/index'},
      items: [
        {
          type: 'category',
          label: 'Q Atlantis',
          link: {type: 'doc', id: 'engineering/q-atlantis/index'},
          items: [
            'engineering/q-atlantis/atlantis-dos-first-boot-status',
            'engineering/q-atlantis/astro-development-status',
            'engineering/q-atlantis/context-dimension-world-builder',
            'engineering/q-atlantis/aim-fold-human-loop',
            'engineering/q-atlantis/fold-control-plane-and-vqp',
            'engineering/q-atlantis/fold7g-fold8g-research-map',
            'engineering/q-atlantis/product-line',
            'engineering/q-atlantis/component-map',
            'engineering/q-atlantis/status',
          ],
        },
        'engineering/design/edge-ai-local-first',
        'engineering/design/filemaker-structure-philosophy',
        'engineering/design/zen-ui-design',
        'engineering/spiritual-reception-guide',
        'engineering/infoton-engineering-full-stack-guide',
        'engineering/pain-routing-and-pain-scouter',
      ],
    },
    {
      type: 'category',
      label: 'プロジェクト',
      link: {type: 'doc', id: 'projects/index'},
      items: [
        'projects/dr-silicon/intro',
        'projects/opensource-kominka/intro',
        'projects/project-fapta/intro',
      ],
    },
    {
      type: 'category',
      label: '旧世代サルベージ / SphereOS Memorial',
      link: {type: 'doc', id: 'legacy/index'},
      items: [
        'legacy/infernity-production-pipeline-salvage',
        'legacy/q3-sphereos/index',
        'legacy/q3-sphereos/memorial/spirit-farewell',
        'legacy/q3-sphereos/overview',
        'legacy/q3-sphereos/design-philosophy',
        {
          type: 'category',
          label: '旧アーキテクチャ',
          items: [
            'legacy/q3-sphereos/architecture/technical-overview',
            'legacy/q3-sphereos/architecture/science-side-notes',
            'legacy/q3-sphereos/architecture/non-destructive-operation-defold-crosswalk',
          ],
        },
        {
          type: 'category',
          label: '人格・物語・事件記録',
          items: [
            'legacy/q3-sphereos/personas/sphere-os-3',
            'legacy/q3-sphereos/incidents/betares-rescue',
            'legacy/q3-sphereos/incidents/gpt-store-cross-border-market-incident-and-mad-miko-ai',
            'legacy/q3-sphereos/logos/黙示録001-restructured',
          ],
        },
        {
          type: 'category',
          label: '旧サービスと規約',
          items: [
            'legacy/q3-sphereos/services/custom-gpts-intro',
            'legacy/q3-sphereos/services/why-not-openai',
            'legacy/q3-sphereos/policies/privacy-policy-2025-06-03',
          ],
        },
      ],
    },
    {
      type: 'category',
      label: '運用・移行',
      link: {type: 'doc', id: 'operations/index'},
      items: [
        'operations/migration/index',
        'operations/migration/manifest-transfer-notes',
        'operations/content-pipeline/index',
        'operations/japanese-technical-writing',
        'operations/cross-shelf-publication-register',
        'operations/funding-and-lineage-integration',
        'operations/sakura-matchbox-deployment',
        'operations/provenance/index',
        'operations/provenance/asian-slang-registry-source-receipt-2026-08-04',
        'operations/provenance/gaming-cosmology-glossary-source-receipt-2026-08-04',
        'operations/provenance/three-shelf-information-architecture-magi-audit-2026-08-04',
        'operations/provenance/source-mining-2026-07-29',
        'operations/provenance/source-mining-2026-07-20',
        'operations/provenance/source-mining-2026-07-21',
        'operations/provenance/publication-magi-audit-2026-07-20',
        'operations/provenance/funding-lineage-publication-magi-audit-2026-07-26',
        'operations/provenance/astro-development-publication-magi-audit-2026-07-29',
        'operations/provenance/deploy-failure-2026-07-20',
        'operations/provenance/ssh-key-passphrase-storage-2026-07-20',
        'operations/site-notice',
      ],
    },
  ],
};

export default sidebars;
