#!/usr/bin/node
const { argv } = require('node:process');
const argument = argv[2] ? argv[2] : null;
if (argument) {
  console.log(argument);
} else {
  console.log('No argument');
}
