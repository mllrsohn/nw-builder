import fs from "node:fs";
import { resolve } from "node:path";
import https from "node:https";

import progress from "cli-progress";

const bar = new progress.SingleBar({}, progress.Presets.rect);

/**
 * Download NW.js binary
 *
 * @param  {string}        version       Version
 * @param  {string}        flavor        Flavor
 * @param  {string}        platform      Platform
 * @param  {string}        architecture  Architecture
 * @param  {string}        downloadUrl   Download url
 * @param  {string}        outDir        Output directory
 * @return {Promise<void>}
 */
const download = (
  version,
  flavor,
  platform,
  architecture,
  downloadUrl,
  outDir,
) => {
  return new Promise((res, rej) => {
    if (downloadUrl !== "https://dl.nwjs.io") {
      rej(new Error("Invalid download url. Please try again."));
    }

    let url = `${downloadUrl}/v${version}/nwjs${
      flavor === "sdk" ? "-sdk" : ""
    }-v${version}-${platform}-${architecture}.${
      platform === "linux" ? "tar.gz" : "zip"
    }`;

    https.get(url, (res) => {
      let chunks = 0;
      bar.start(Number(res.headers["content-length"]), 0);

      res.on("data", (chunk) => {
        chunks += chunk.length;
        bar.increment();
        bar.update(chunks);
      });

      res.on("error", (error) => {
        rej(error);
      });

      res.on("end", () => {
        bar.stop();
        res();
      });

      fs.mkdirSync(outDir, { recursive: true });
      const stream = fs.createWriteStream(
        resolve(outDir, `nw.${platform === "linux" ? "tar.gz" : "zip"}`),
      );
      res.pipe(stream);
    });
  });
};

export { download };
