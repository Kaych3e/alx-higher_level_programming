#!/usr/bin/node
// script that prints a square
// The first argument is the size of the square
// If first argument can’t convert to an integer, print “Missing size”

const n = parseInt(process.argv[2]);

if (isNaN(n)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < n; i++) {
    let row = '';
    for (let j = 0; j < n; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
