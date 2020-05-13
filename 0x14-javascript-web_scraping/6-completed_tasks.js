#!/usr/bin/node

const request = require('request');
const name = '?completed=true';
const dir = process.argv[2];
const url = (dir + name);
request.get(url, function (error, response, body) {
  let data = {};
  if (error) {
    console.log(error);
  }
  data = (JSON.parse(body));
  function obtain (data) {
    const dict = {};
    let i = 1; let j = 0;
    for (const user in data) {
      for (const valor in user) {
        if (valor.userId === i) {
          j += 1;
          console.log('entra');
        }
        dict[i] = j;
      }
      i++;
    }
    console.log(dict);
  }
  obtain(data);
}
);
