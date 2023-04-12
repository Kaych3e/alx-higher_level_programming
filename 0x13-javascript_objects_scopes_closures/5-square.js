#!/usr/bin/node

const Rectangle = require('./4-rectangle');
// defines a square that inherits from Rectangle class

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
