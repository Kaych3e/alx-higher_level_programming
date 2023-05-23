#!/usr/bin/node
// Script that displays status code of GET request

// import request and request URL
const request = require('request');
const url = process.argv[2];

request(url, (error, response, data) => {
  if (error) {
    console.log(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
