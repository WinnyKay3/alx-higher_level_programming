#!/usr/bin/node

const process = require('process');
const firstArg = process.argv[2];
const size = parseInt(firstArg);

if (!isNaN(size)) {
  if (size > 0) {
    for (let k = 0; k < size; k++) {
      let row = '';
      for (let m = 0; m < size; m++) {
        row += 'X';
      }
      console.log(row);
    }
  }
} else {
  console.log('Missing size');
}
