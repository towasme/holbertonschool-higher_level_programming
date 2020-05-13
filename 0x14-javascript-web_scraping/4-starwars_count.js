#!/usr/bin/node

const request = require('request');
const name = process.argv[2];
const url = ('https://swapi-api.hbtn.io/api/films/' + name);

request.get(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  console.log(JSON.parse(body).title);
});
