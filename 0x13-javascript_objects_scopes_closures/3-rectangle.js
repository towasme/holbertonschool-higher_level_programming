#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w < 0 || h < 0) {
    } else if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // method
  print () {
    let i = 0;
    const num = 'X';
    for (i; i < this.height; i++) {
      console.log(num.repeat(this.width));
    }
  }
}
module.exports = Rectangle;
