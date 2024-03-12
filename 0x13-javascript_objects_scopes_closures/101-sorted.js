#!/usr/bin/node
const { dict } = require('./101-data');
const userIds = [];

Object.values(dict).forEach((user) => {
  console.log(user);
  if (!userIds.includes(user)) {
    userIds.push(user);
  }
});

const people = userIds.reduce((acc, userId) => {
  acc[userId] = [];
  Object.entries(dict).forEach((entry) => {
    const [key, value] = entry;
    if (value === userId) {
      acc[userId].push(key);
    }
  });
  return acc;
}, {});

console.log(dict);
console.log(people);
