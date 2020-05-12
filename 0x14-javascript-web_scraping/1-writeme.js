#!/usr/bin/node

const fs = require('fs');
const fileName = process.argv[2];
const data = process.argv[3];
// write on the file
fs.writeFile(fileName, data, 'utf-8', (error) => {
  if (error) {
    return console.log(error);
  }
  console.log(data);
});
