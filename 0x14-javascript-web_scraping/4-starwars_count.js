#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const result = (JSON.parse(body).results);
  let cont = 0;
  for (const movie of result) {
    for (const chara of movie.characters) {
      if (chara.includes('18')) {
        cont += 1;
      }
    }
  }
  console.log(cont);
});
