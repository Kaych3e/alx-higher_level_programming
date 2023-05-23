#!/usr/bin/node
// script that gets the contents of a webpage and stores it in a file

const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const filePath = process.argv[3];

request(url, 'utf-8', (error, response, data) => {
  if (error) {
    console.log(error);
    return;
  }
  fs.writeFile(filePath, data, (error) => {
    if (error) {
      console.log(error);
    }
  });
});
