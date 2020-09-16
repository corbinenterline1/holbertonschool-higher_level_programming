#!/usr/bin/node
// Computes & prints a factorial
isNaN(process.argv[2]) ? console.log(1) : console.log(factrecursial(process.argv[2]));

function factrecursial (a) {
  if (a === 0) {
    return 1;
  } else {
    return a * factrecursial(a - 1);
  }
}
