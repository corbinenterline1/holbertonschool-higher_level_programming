#!/usr/bin/node
// Prints status code of a GET request. First arg is URL.
const request = require('request');
request(process.argv[2], function (err, response, body) {
  if (err) {
    console.log('error:', err);
  }
  console.log('code:', response.statusCode);
});
