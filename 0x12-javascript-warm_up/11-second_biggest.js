#!/usr/bin/node
// Searches for second biggest integer in list of args
if (process.argv.length <= 2) {
  console.log(0);
} else {
  const args = process.argv.slice(2);
  args.sort(function (a, b) { return b - a; });
  console.log(args);
  console.log(args[1]);
}
