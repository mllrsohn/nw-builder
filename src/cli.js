#!/usr/bin/env node

import { program } from 'commander';

import nwbuild from './index.js';

program
  .argument('<string>', 'File path(s) to project')
  .option('--mode <string>', 'get, run or build mode', 'build')
  .option('--version <string>', 'NW.js version', 'latest')
  .option('--flavor <string>', 'NW.js build flavor', 'normal')
  .option('--platform <string>', 'NW.js supported platform')
  .option('--arch <string>', 'NW.js supported architecture')
  .option('--downloadUrl <string>', 'NW.js download server')
  .option('--manifestUrl <string>', 'NW.js version info')
  .option('--cacheDir <string>', 'Cache NW.js binaries')
  .option('--outDir <string>', 'NW.js build artifacts')
  .option('--app <object>', 'Platform specific app metadata. Refer to docs for more info')
  .option('--cache <boolean>', 'Flag to enable/disable caching', true)
  .option('--ffmpeg <boolean>', 'Flag to enable/disable downloading community ffmpeg', false)
  .option('--glob <boolean>', 'Flag to enable/disable globbing', true)
  .option('--logLevel <string>', 'Specify log level')
  .option('--zip <string>', 'Flag to enable/disable compression', false)
  .option('--managedManifest <string>', 'Managed manifest mode', false)
  .option('--nodeAddon <boolean>', 'Download NW.js Node headers', false);

program.parse();

console.log(program.args.join(' '))
console.log(program.opts())
nwbuild({
  ...program.opts(),
  srcDir: program.args.join(' '),
  cli: true,
});
