#!/usr/bin/node

class Rectangle {
  constructor(w, h) {
    if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
      return {};
    }

    // setting instance attributes
    this.width = w;
    this.width = h;
  }

  // creates instance method print() to print the rectangle with X
  print () {
    let row = '';
    for (let i = 0; i < this.width; i++) {
      row += 'X';
    }
    for (let j = 0; j < this.height; j++) {
      console.log(row);
    }
  }

  // creates instance method rotate() and double()
  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
