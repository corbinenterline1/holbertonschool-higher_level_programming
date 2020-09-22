#!/usr/bin/node
// Creates a class Square that inherits from Rectangle
// Gotta extends, take a size, and use super for dat rect
// add instance method charPrint(c), prints using c
class Square extends require('./5-square') {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.width; i++) {
        console.log(c.repeat(this.height));
      }
    }
  }
}
module.exports = Square;
