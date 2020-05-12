#!/usr/bin/node

const fs = require('fs');
const fileName = process.argv[2];
// read the file
fs.readFile(fileName, 'utf-8', (error, data) => {
  if (error) {
    return console.log(error);
  }
  // invoke the data
  console.log(data);
});
