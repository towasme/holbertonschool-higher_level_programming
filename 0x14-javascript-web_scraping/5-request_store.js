#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const fileName = process.argv[3];
const url = process.argv[2];
// extract info
request.get(url, function (error, body) {
  if (error) {
    console.log(error);
  }
}).pipe(fs.createWriteStream(fileName, 'utf-8'));
