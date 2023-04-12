#!/usr/bin/node
// script that searches the second biggest integer in the list of arguments
// If no argument passed or number or arg is 1, print 0

function secondInt (arg) {
  const array = args.map(x => parseInt(x)).sort((a, b) => b - a);
  return array[1] || 0;
}

const args = process.argv.slice(2);
console.log(secondInt(args));
