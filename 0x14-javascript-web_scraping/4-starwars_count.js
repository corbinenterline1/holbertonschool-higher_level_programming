#!/usr/bin/node
//WEDGE ANTILLES, IT'S YOUR TIME
const request = require('request');
request(process.argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
  }
  let wedge = 0;
  const fds = JSON.parse(body);
  for (let i = 0; i < fds.results.length; i++) {
    for (let j = 0; j < fds.results[i].characters.length; j++) {
      if (fds.results[i].characters[j].includes('18')) {
        wedge++;
      }
    }
  }
  console.log(wedge);
});
