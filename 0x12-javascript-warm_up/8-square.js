#!/usr/bin/node

const number = parseInt(process.argv[2]);
let i = 0;
let j = 0;
let pound = '';

if (number) {
  while (i < (process.argv[2])) {
    while (j < (process.argv[2])) {
      pound += 'X';
      j++;
    }
    console.log(pound);
    pound = '';
    j = 0;
    i++;
  }
} else {
  console.log('Missing size');
}
