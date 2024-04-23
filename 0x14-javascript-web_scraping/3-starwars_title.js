#!/usr/bin/node
// Script that display the status code of a GET request
const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const movie = JSON.parse(body);
    console.log(movie.title);
  }
});