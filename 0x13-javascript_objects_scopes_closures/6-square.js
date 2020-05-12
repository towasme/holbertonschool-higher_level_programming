#!/usr/bin/node
const Square5 = require('./5-square');

module.exports = class Square extends Square5 {
  // method print in c
  charPrint (c) {
    let i = 0;
    if (c === undefined) {
      c = 'X';
    }
    for (i; i < this.size; i++) {
      console.log(c.repeat(this.size));
    }
  }
};
