#!/usr/bin/node
// script that prints a message depending of the number of arguments passed

const args = process.argv.slice(2);
//passes the argument to the script

if (args.length === 0) {
  console.log('No argument');
} else if (args.length === 1) {
  console.log('Argument found');
} else {
  console.log(`${args.length} Arguments found`);
}
