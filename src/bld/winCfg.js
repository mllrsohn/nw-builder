import { rename } from "node:fs/promises";

import rcedit from "rcedit";

import { log } from "../log.js";

/**
 * Windows specific configuration steps
 * https://learn.microsoft.com/en-us/windows/win32/msi/version
 * https://learn.microsoft.com/en-gb/windows/win32/sbscs/application-manifests
 * https://learn.microsoft.com/en-us/previous-versions/visualstudio/visual-studio-2015/deployment/trustinfo-element-clickonce-application?view=vs-2015#requestedexecutionlevel
 * https://learn.microsoft.com/en-gb/windows/win32/menurc/versioninfo-resource
 *
 * @param {import("../nwbuild").App} app     Multi platform configuration options
 * @param {string}                   outDir  The directory to hold build artifacts
 */
const setWinConfig = async (app, outDir) => {
  let versionString = {
    Comments: app.comments,
    CompanyName: app.companyName,
    FileDescription: app.fileDescription,
    FileVersion: app.fileVersion,
    InternalName: app.internalName,
    LegalCopyright: app.legalCopyright,
    LegalTrademarks: app.legalTrademark,
    OriginalFilename: app.originalFilename,
    PrivateBuild: app.privateBuild,
    ProductName: app.productName,
    ProductVersion: app.productVersion,
    SpecialBuild: app.specialBuild,
  };

  Object.keys(versionString).forEach((option) => {
    if (versionString[option] === undefined) {
      delete versionString[option];
    }
  });

  try {
    await rename(`${outDir}/nw.exe`, `${outDir}/${app.name}.exe`);

    await rcedit(`${outDir}/${app.name}.exe`, {
      "file-version": app.version,
      "icon": app.icon,
      "product-version": app.version,
      "version-string": versionString,
    });
  } catch (error) {
    log.warn(
      "Unable to modify EXE. Ensure WINE is installed or build in Windows",
    );
    log.error(error);
  }
};

export { setWinConfig };
