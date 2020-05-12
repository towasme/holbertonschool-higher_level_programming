#!/usr/bin/node

exports.converter = function (base) {
  return function Changes (n) {
    return (n.toString(base));
  };
};
