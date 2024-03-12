#!/usr/bin/node
exports.converter = function (number) {
  return (num) => num.toString(number);
};
