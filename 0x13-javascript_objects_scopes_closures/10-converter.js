#!/usr/bin/node
// Function that converts number from base 10 to another base (passed arg)
exports.converter = function (base) {
  return function (num) {
    return num.toString(base);
  };
};
