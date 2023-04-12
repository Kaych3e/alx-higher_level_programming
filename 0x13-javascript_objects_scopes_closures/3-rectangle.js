#!/usr/bin/node

class Rectangle {
  constructor(w, h) {
    if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
      return {};
    }
// sets instance attribute of height and width with "this" keyword

    this.width = w;
    this.height = h;
  }

// creates instance method called print() that prints the rectangle

  print() {
    let row = '';
    for (let i = 0; i < this.width; i++) {
      row += 'X';
    }
    for (let i = 0; i < this.height; i++) {
        console.log(row);
    }
  }
}
