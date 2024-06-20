#!/usr/bin/node

function add (a, b) {
  return a + b;
}

// To make the function visible from outside
module.exports.add = add;
