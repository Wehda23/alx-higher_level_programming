#!/usr/bin/node
// Script that display the status code of a GET request
const request = require('request');
const url = process.argv[2];
const path = process.argv[3];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const movies = JSON.parse(body);
    fs.writeFileSync(path, movies, 'utf-8');
    }
});
