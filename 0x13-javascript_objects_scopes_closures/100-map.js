#!/usr/bin/node

// imports array from 100-data.js
const list = require('./100-data').list;

// create new array using map() method
const newList = list.map((value, index) => value * index);

console.log(list);
console.log(newList);
