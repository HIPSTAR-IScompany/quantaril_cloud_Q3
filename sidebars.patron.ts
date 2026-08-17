import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

const sidebars: SidebarsConfig = {
  patronSidebar: [
    'index',
    {
      type: 'category',
      label: '奉納・協賛方法',
      link: {type: 'doc', id: 'give/index'},
      items: ['give/physical', 'give/hipstar-infra', 'give/feeding', 'give/commons'],
    },
    {
      type: 'category',
      label: '玉垣協賛広告',
      link: {type: 'doc', id: 'tamagaki/index'},
      items: ['tamagaki/current', 'tamagaki/archive'],
    },
    'supply/index',
    'media/index',
    {
      type: 'category',
      label: 'Policy',
      link: {type: 'doc', id: 'policy/index'},
      items: [
        'policy/attribution',
        'policy/sponsorship',
        'policy/content-adjacency',
        'policy/scope-and-liability',
        'policy/data-and-privacy',
      ],
    },
  ],
};

export default sidebars;
