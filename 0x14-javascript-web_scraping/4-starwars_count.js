#!/usr/bin/node
// Script that prints the number of movies
// where the character Wedge Antilles is present.

// import request and request URL
const request = require('request');
const url = process.argv[2];
const character = 'https://swapi-api.alx-tools.com/api/people/18/';

request(url, (error, response, data) => {
  if (error) {
    console.log(error);
  } else {
    const movie = (JSON.parse(data).results);
    const match = movie.filter((film) => film.characters.includes(character));
    console.log(`${match.length}`);
  }
});
