#!/usr/bin/node
// Prints x times C is fun
if (isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  let i = 1;
  const num = parseInt(process.argv[2], 10);
  while (i <= num) {
    console.log('C is fun');
    i++;
  }
}
