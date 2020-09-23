#!/usr/bin/node
// Computes number of tasks completed by user id. First arg is api url.
// Only show users with completed tasks (no slackers)
const request = require('request');
request(process.argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
  }
  const users = {};
  const bds = JSON.parse(body);
  for (let i = 0; i < bds.length; i++) {
    if (bds[i].completed) {
      if (users[bds[i].userId]) {
        users[bds[i].userId] += 1;
      } else {
        users[bds[i].userId] = 1;
      }
    }
  }
  console.log(users);
});
