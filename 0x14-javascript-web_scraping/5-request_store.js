#!/usr/bin/node
// Writes webpage to file, first arg is URL
// 2nd arg is filepath, utf-8
const fs = require('fs');
const request = require('request');
request(process.argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
  }
  fs.writeFile(process.argv[3], body, 'utf-8', function (err, body) {
    if (err) {
      console.log(err);
    }
  });
});
