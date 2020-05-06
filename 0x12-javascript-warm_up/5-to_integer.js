#!/usr/bin/node

const number = Number.isNaN(parseInt(process.argv[2]));

if (number) {
  console.log('Not a number');
} else {
  console.log('My number: %d', parseInt(process.argv[2]));
}
