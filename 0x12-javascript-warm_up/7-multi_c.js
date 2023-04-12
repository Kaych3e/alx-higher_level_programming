#!/usr/bin/node
// script that prints x times “C is fun”
// If the first argument can’t be converted to an integer,
// print “Missing number of occurrences”

const args = process.argv.slice(2);
const x = parseInt(args[0]);

if (isNaN(x)) {
  console.log('Missing number of occurences');
} else {
  let i = 0;
  while (i < x) {
    console.log('C is fun');
    i++;
  }
}
