#!/usr/bin/node

// import dict object from 101-data file
const dict = require('./101-data').dict;

// create new object with reduce() method
const newDict = Object.keys(dict).reduce((acc, key) => {
  const value = dict[key];
  if (acc[value]) {
    acc[value].push(key);
  } else {
    acc[value] = [key];
  }
  return acc;
}, {});

console.log(newDict);
