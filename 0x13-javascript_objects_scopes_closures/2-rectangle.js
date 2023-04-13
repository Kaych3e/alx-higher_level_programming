#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
    // initialising instance attributes of width and height
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
