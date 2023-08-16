#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) { [this.width, this.height] = [w, h]; }
  }

  print () {
    for (let k = 0; k < this.height; k++) console.log('X'.repeat(this.width));
  }

  rotate () {
    [this.height, this.width] = [this.width, this.height];
  }

  double () {
    [this.width, this.height] = [this.width * 2, this.height * 2];
  }
};
