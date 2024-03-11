#!/usr/bin/node

const addMeMaybe = (number, thefunction) => {
  thefunction(++number);
};

exports.addMeMaybe = addMeMaybe;
