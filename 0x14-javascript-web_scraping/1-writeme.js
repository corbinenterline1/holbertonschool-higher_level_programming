#!/usr/bin/node
// Writes string to a file, utf-8, same err handling as 0
const fs = require('fs');
fs.writeFile(process.argv[2], process.argv[3], function (err) {
  if (err) {
    console.log(err);
  }
});
