#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
request.get(url, function (error, response, body) {
  let data = {};
  if (error) {
    console.log(error);
  }
  data = (JSON.parse(body));
  function obtain (data) {
    const dict = {};
    let i = 0; let j = 0; let k = 1;
    const user = [];
    // const obj = Object;
    //   for (user of data) {
    //     if (Object.prototype.hasOwnProperty.call(obj, user.userId)) {
    //       obj[user.userId] += 1;
    //     } else {
    //       obj[user.userId] = 1;
    //     }
    //   }
    //   console.log(obj);
    // }
    data.forEach(element => {
      if (element.completed === true) {
        user[i] = (element.userId);
        i++;
      }
    });
    i = 0;
    while (user[j] === k && user[j] !== undefined) {
      i += 1;
      j++;
      if (user[j] !== k) {
        dict[k] = i;
        i = 0;
        k++;
      }
    }
    console.log(dict);
  }
  obtain(data);
});
