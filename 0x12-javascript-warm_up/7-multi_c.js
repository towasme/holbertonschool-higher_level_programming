#!/usr/bin/node

const number = parseInt(process.argv[2]);
let i = 0;

if (number) {
  while (i < (process.argv[2])) {
    console.log('C is fun');
    i++;
  }
} else {
  console.log('Missing number of occurrences');
}
