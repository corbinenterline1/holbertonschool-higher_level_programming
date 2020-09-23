#!/usr/bin/node
// Reads & prints contents of a file, utf-8, print error object if bad
const fs = require('fs');
fs.readFile(process.argv[2], 'utf-8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
