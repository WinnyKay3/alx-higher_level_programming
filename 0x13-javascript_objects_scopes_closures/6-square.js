#!/usr/bin/node

const Rectangle = require('./5-square');

module.exports = class Square extends Rectangle {
  constructor (size) {
     super(size, size);
   }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let k = 0; k < this.width; k++) {
      let row = '';
      for (let n = 0; n < this.height; n++) {
	 row += c;
       }
       console.log(row);
     }
   }
};
