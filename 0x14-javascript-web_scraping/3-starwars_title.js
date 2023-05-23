#!/usr/bin/node
// Script that prints the title of a Star Wars movie

// import request and request URL
const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;

request(url, (error, response, data) => {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(data).title);
  }
});
