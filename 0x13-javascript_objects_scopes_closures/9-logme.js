#!/usr/bin/node
// Function that prints the number of args already printed & new arg value
let i = 0;
exports.logMe = function (item) {
  console.log(`${i}: ${item}`);
  i++;
};
