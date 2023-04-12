#!/usr/bin/node

class Square extends require('./5-square.js') {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let squareString = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        squareString += c;
      }
      squareString += '\n';
    }
    console.log(squareString);
  }
}

module.exports = Square;
