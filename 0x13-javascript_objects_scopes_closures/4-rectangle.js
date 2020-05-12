#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w < 0 || h < 0) {
    } else if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // method print
  print () {
    let i = 0;
    const num = 'x';
    for (i; i < this.height; i++) {
      console.log(num.repeat(this.width));
    }
  }

  // method rotate
  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  // method double
  double () {
    this.width = (this.width * 2);
    this.height = (this.height * 2);
  }
}
module.exports = Rectangle;
