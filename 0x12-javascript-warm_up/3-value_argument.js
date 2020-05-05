#!/usr/bin/node
const args = process.argv[2];
let print = 'No argument';
if (args !== undefined) {
  print = process.argv[2];
}
console.log(print);
