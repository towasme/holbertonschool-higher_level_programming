#!/usr/bin/node

const args = process.argv.length;

if (args > 3) {
  console.log(process.argv.sort((a, b) => a - b).reverse()[1]);
} else {
  console.log('0');
}
