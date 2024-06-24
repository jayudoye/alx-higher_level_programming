#!/usr/bin/node

const process = require('process');
const args = process.argv;

let numFactorial;

function recursion (n) {
  if (n === 1) {
    return 1;
  } else {
    return n * recursion(n - 1);
  }
}

if (args.length < 3 || isNaN(args[2])) {
  console.log(1);
} else {
  numFactorial = recursion(args[2]);
  console.log(numFactorial);
}
