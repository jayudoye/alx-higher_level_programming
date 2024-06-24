#!/usr/bin/node

const arg1 = process.argv[2];
const arg2 = process.argv[3];

add(arg1, arg2);

function add (a, b) {
  console.log(parseInt(a) + parseInt(b));
}
