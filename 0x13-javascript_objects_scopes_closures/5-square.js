#!/usr/bin/node

class Rectangle {
  constructor(w, h) {
    if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
      return {};
    }

// creates instance attribtutes for width and height

    this.width = w;
    this.height = h;
  }

// creates instance methods print(), rotate() and double() that can be called

  rotate() {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double() {
    this.width *= 2;
    this.height *= 2;
  }
}

class Square extends Rectangle {
  constructor(size) {
    super(size, size);
  }
}
