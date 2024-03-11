#!/usr/bin/node
const { argv } = require('node:process');
const argument = parseInt(argv[2]);
if (argument) {
  console.log(`My number: ${argument}`);
} else {
  console.log('Not a number');
}
