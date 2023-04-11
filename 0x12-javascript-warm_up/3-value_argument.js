#!/usr/bin/node
// Script that prints the first argument passed to it with console.log
// No use of 'var' and 'length'

const args = process.argv.slice(2);
const Arg1 = args[0];
// passes the argument to the script and checks if true or false

if (!Arg1) {
  console.log(Arg1);
} else {
  console.log('No Argument');
}
