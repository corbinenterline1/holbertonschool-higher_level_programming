#!/usr/bin/node
// Function that returns the reversed version of a list
exports.esrever = function (list) {
  const rev = [];
  while (list.length) {
    rev.push(list.pop());
  }
  return rev;
};
