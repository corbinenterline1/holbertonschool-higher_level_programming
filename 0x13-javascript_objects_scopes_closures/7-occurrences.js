#!/usr/bin/node
// Function that returns the number of occurrences in a list
exports.nbOccurences = function (list, searchElement) {
  let i = 0;
  for (const item in list) {
    if (list[item] === searchElement) {
      i++;
    }
  }
  return i;
};
