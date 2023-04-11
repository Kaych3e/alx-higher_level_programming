#!/usr/bin/node
// script that prints My number: <first argument converted in integer>
// if the first argument can be converted to an integer:
// If the argument can’t be converted, print “Not a number”

const arg = process.argv[2];
const num = parseInt(arg);
// changes arg to an integer and assigns it to constant num

if (Number.isNaN(num)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${num}`);
}
  
