#!/usr/bin/node
// Script that display the status code of a GET request
const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body).characters;
    for (let i = 0; i < data.length; i++) {
      const character = data[i];
      request(character, function (error, response, body) {
        if (error) {
          console.log(error);
        } else {
          const name = JSON.parse(body).name;
          console.log(name);
        }
      }
      );
    }
  }
});
