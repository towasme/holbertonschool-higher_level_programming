#!/usr/bin/node

exports.esrever = function (list) {
  let i = (list.length - 1);
  const newlist = [];
  for (i; i >= 0; i--) {
    newlist.push(list[i]);
  }
  return (newlist);
};
