#!/usr/bin/node
let line = 0;

exports.logMe = function (message) {
  console.log(`${line++}: ${message}`);
};
