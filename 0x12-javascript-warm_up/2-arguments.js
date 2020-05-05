#!/usr/bin/node

let numarg = 'No argument';
const args = process.argv.length;
if (args === 2) {
  console.log(numarg);
} else if (args === 3) {
  numarg = 'Argument found';
  console.log(numarg);
} else {
  numarg = 'Arguments found';
  console.log(numarg);
}
