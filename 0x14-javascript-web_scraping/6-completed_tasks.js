#!/usr/bin/node
// Script that display the status code of a GET request
const request = require('request');
const url = process.argv[2];


request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    const completedUser = {};

    for (let i = 0; i < data.length; i++)
    {
    const userId = body[i].userId;
    const completed = body[i].completed;

    if (completed && !completedUser[userId])
    {
    completedUser[userId] = 0;
    }

    if (completed)
    {
    completedUser[userId]++;
    }
    }
    console.log(completedUser);
  }
});
