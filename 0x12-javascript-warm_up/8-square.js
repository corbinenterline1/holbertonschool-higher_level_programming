#!/usr/bin/node
// Print a square in javascript! This used to be hard LOL
if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  let square = '';
  const num = parseInt(process.argv[2], 10);
  for (let i = 0; i < num; i++) {
    for (let j = 0; j < num; j++) {
      square += 'X';
    }
    if (i !== num - 1) {
      square += '\n';
    }
  }
  console.log(square);
}
