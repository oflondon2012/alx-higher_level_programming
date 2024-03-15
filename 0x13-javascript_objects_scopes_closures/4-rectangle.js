#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w >= 1 && h >= 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let row = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        row = row + 'X';
      }
      console.log(row);
      row = '';
    }
  }

  rotate () {
    const teme = this.width;
    this.width = this.height;
    this.height = teme;
  }

  double () {
    this.width = this.width * 2;
    this.heigth = this.heigth * 2;
  }
};
