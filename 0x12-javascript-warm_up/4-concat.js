#!/usr/bin/node
// script that prints two arguments passed to it, in the following format: is

const args = process.argv.slice(2);
const arg1 = args[0];
const arg2 = args[1];
// Assigning arguments to variables

if (arg1 && arg2) {
  console.log(`${arg1} is ${arg2}`);
} else {
  console.log('undefined');
}
