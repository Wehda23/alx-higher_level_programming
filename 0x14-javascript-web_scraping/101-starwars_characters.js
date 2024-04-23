#!/usr/bin/node
// Script that display the status code of a GET request
const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body).characters;
    const ordered = {};
    const promises = [];

    for (let i = 0; i < data.length; i++) {
      const character = data[i];
      const characterId = character.split("/")[5];
      const promise = new Promise((resolve, reject) => {
        request(character, function (error, response, body) {
          if (error) {
            reject(error);
          } else {
            const name = JSON.parse(body).name;
            resolve({ characterId, name });
          }
        });
      });
      promises.push(promise);
    }

    Promise.all(promises)
      .then(results => {
        results.forEach(result => {
          ordered[result.characterId] = result.name;
        });
        console.log(ordered);
      })
      .catch(error => {
        console.log(error);
      });

    for (let j = 0; j < data.length ; j++)
    {
        const userId = data[j].split("/")[5];
        console.log(ordered[userId]);
    }
  }
});
