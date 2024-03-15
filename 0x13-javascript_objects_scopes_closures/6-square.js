#!/usr/bin/node
const newsquare = require('./5-square.js');
module.exports = class Square extends newsquare {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    let rows = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        rows = rows + c;
      }
      console.log(rows);
      rows = '';
    }
  }
};
