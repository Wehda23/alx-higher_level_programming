#!/usr/bin/node
// Script that display the status code of a GET request
const request = require('request');
const url = process.argv[2];
let count = 0;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const movies = JSON.parse(body).results;
    for (let i = 0; i < movies.length; i++) {
	    const characters = movies[i].characters;
	    for (let j = 0; j < characters.length; j++) {
		    const character = characters[j];
		    const characterId = character.split('/')[5];
		    if (characterId === '18') {
          count++;
		    }
	    }
    }
  }

  console.log(count);
});
