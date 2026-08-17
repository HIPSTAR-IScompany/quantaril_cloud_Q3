import { themes as prismThemes } from 'prism-react-renderer';
import type { Config } from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

const legacyRedirects = require('./migration/redirects.json');

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)
const config: Config = {

  title: 'Q Atlantis',
  tagline: '神話・人格・体験・技術を、次の世界へ運ぶ',
  titleDelimiter: '·',
  favicon: 'img/favicon.ico',

  // Set the production url of your site here
  url: 'https://quantaril.cloud',
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  // Productionとlocal previewはどちらもdocument rootで配信する。
  // NODE_ENVでbaseUrlを変えると、production buildを`docusaurus serve`した際に
  // HTMLは`/assets/...`、serve側だけ`/dev/`という二重定規になりCSS/JSが壊れる。
  baseUrl: '/',

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: 'HIPSTAR', // Usually your GitHub org/user name.
  projectName: 'quantaril', // Usually your repo name.

  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',

  i18n: {
    defaultLocale: 'ja',
    locales: ['ja'],
  },

  headTags: [
    {
      tagName: 'script',
      attributes: {
        type: 'application/ld+json',
      },
      innerHTML: JSON.stringify({
        '@context': 'https://schema.org',
        '@type': 'WebSite',
        name: 'Q Atlantis',
        alternateName: 'Quantaril Cloud Q Atlantis',
        url: 'https://quantaril.cloud/',
        description: '神話・人格・体験・技術を一つの正しさへ潰さず、World・Fold・OAEとして運ぶ公開研究鍛造所。',
        inLanguage: 'ja',
        image: 'https://quantaril.cloud/img/quantaril-social-card-atlantis.png',
        sameAs: [
          'https://x.com/K_chachamaru',
          'https://github.com/HIPSTAR-IScompany/quantaril_cloud_QAtlantis',
        ],
      }),
    },
  ],

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.ts',
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          editUrl: undefined,
          //  'https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/',
        },
        blog: {
          showReadingTime: true,
          feedOptions: {
            type: ['rss', 'atom'],
            xslt: true,
          },
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          editUrl: undefined,
          //  'https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/',
          // Useful options to enforce blogging best practices
          onInlineTags: 'ignore',
          onInlineAuthors: 'warn',
          onUntruncatedBlogPosts: 'ignore',
        },
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],
  markdown: {
    mermaid: true,
  },
  themes: ['@docusaurus/theme-mermaid'],
  plugins: [
    './plugins/patron-data-export/index.mjs',
    [
      '@docusaurus/plugin-client-redirects',
      {
        redirects: legacyRedirects,
      },
    ],
    [
      '@docusaurus/plugin-content-docs',
      {
        id: 'about',
        path: 'about',
        routeBasePath: 'about',
        sidebarPath: require.resolve('./sidebars.about.ts'),
      },
    ],
    [
      '@docusaurus/plugin-content-docs',
      {
        id: 'reference',
        path: 'reference',
        routeBasePath: 'reference',
        sidebarPath: require.resolve('./sidebars.reference.ts'),
      },
    ],
    [
      '@docusaurus/plugin-content-docs',
      {
        id: 'glossary',
        path: 'glossary',
        routeBasePath: 'glossary',
        sidebarPath: require.resolve('./sidebars.glossary.ts'),
      },
    ],
  ],

  themeConfig: {
    mermaid: {
      theme: { light: 'neutral', dark: 'forest' },
    },
    htmlLang: 'ja',
    colorMode: {
      defaultMode: 'dark',
      disableSwitch: true,
      respectPrefersColorScheme: true,
    },
    image: 'img/quantaril-social-card-atlantis.png',
    metadata: [
      {
        name: 'keywords',
        content: 'Q Atlantis, SphereOS, 情報子工学, 意味資源OS, Fold, OAE, Gaming Cosmology, オープンサイエンス, OSS',
      },
      {name: 'author', content: '齋藤みつる'},
      {name: 'theme-color', content: '#071827'},
      {property: 'og:site_name', content: 'Q Atlantis'},
      {name: 'twitter:site', content: '@K_chachamaru'},
      {name: 'twitter:creator', content: '@K_chachamaru'},
    ],
    navbar: {
      title: 'Q Atlantis',
      logo: {
        alt: 'quantaril.cloud Logo',
        src: 'img/logo.png',
      },
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'aboutSidebar', // ← about用サイドバーID
          docsPluginId: 'about',      // ← plugin-content-docsのid
          position: 'left',
          label: 'About / 毛玉文化圏',
        },
        {
          type: 'docSidebar',
          sidebarId: 'projectSidebar',
          position: 'left',
          label: '文書庫',
        },
        {
          type: 'docSidebar',
          sidebarId: 'referenceSidebar',
          docsPluginId: 'reference',
          position: 'left',
          label: 'リファレンス',
        },
        {
          type: 'docSidebar',
          sidebarId: 'glossarySidebar',
          docsPluginId: 'glossary',
          position: 'left',
          label: '用語集',
        },
        { to: '/blog', label: 'Blog', position: 'left' },
        {
          href: 'https://github.com/saitoomituru/ZeroRoomLab-manifest',
          label: 'ZeroRoomLab',
          position: 'left',
        },
        {
          href: 'https://github.com/HIPSTAR-IScompany',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: '目的',
          items: [
            {
              label: 'Q Atlantisへようこそ',
              to: '/about/intro',
            },
          ],


        },
        {
          title: 'Community',
          items: [
            {
              label: 'X',
              href: 'https://x.com/K_chachamaru',
            },
          ],
        },
        {
          title: 'More',
          items: [
            {
              label: 'サイト上の表現と免責',
              to: '/docs/operations/site-notice',
            },
            {
              label: 'Blog',
              to: '/blog',
            },
            {
              label: 'GitHub',
              href: 'https://github.com/saitoomituru',
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} quantaril.cloud, HIPSTAR.`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
