#!/usr/bin/node
// Creates a class Square that inherits from Rectangle
// Gotta extends, take a size, and use super for dat rect
class Square extends require('./4-rectangle') {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Square;
