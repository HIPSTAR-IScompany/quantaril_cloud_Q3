import {copyFile, mkdir} from 'node:fs/promises';
import path from 'node:path';

const publicFiles = ['ledger.json', 'activity.json', 'media.json', 'supply.json', 'tamagaki.json'];

export default function patronDataExportPlugin(context) {
  const sourceDirectory = path.join(context.siteDir, 'data', 'patron');

  return {
    name: 'q-atlantis-patron-data-export',
    async postBuild({outDir}) {
      const destinationDirectory = path.join(outDir, 'patron', 'data');
      await mkdir(destinationDirectory, {recursive: true});
      await Promise.all(
        publicFiles.map((fileName) =>
          copyFile(
            path.join(sourceDirectory, fileName),
            path.join(destinationDirectory, fileName),
          ),
        ),
      );
    },
  };
}
