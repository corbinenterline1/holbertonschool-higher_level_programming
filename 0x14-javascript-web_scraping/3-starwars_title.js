#!/usr/bin/node
// Prints title of Star wars movie using SWAPI, by episode number
const request = require('request');
request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
  }
  console.log(JSON.parse(body).title);
});
