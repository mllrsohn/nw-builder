/**
 * @file    Determines if files are already cached locally.
 * @author  ayushmxn
 */

import fs from 'fs';
import path from 'path';

/**
 * Determines if files are already cached locally.
 *
 * @param  {string}   filePath  The directory the files are stored in
 * @param  {string[]} files     The files to validate if cached
 * @return {boolean}            false = missing, true = cached
 */
const checkCache = (filePath, files) => {
  let missing = false;

  // If NW.js is above v0.12.3, then we don't know which files we want from the archives. So just check that the folder exists and has at least 3 files in it.
  if (files.length === 1 && files[0] === '*') {
    return fs.existsSync(filePath) && fs.readdirSync(filePath).length >= 2;
  }

  for (let file of files) {
    if (missing) {
      return false;
    }
    if (!fs.existsSync(path.join(filePath, file))) {
      missing = true;
    }
  }

  return !missing;
};

export default checkCache;
