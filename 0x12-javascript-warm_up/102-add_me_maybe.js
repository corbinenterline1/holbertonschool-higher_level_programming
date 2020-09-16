#!/usr/bin/node
// Increments & calls a function
exports.addMeMaybe = function (number, theFunction) {
  theFunction(number + 1);
};
