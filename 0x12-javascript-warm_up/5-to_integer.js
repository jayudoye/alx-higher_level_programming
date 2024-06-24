#!/usr/bin/node

const firstArgument = process.argv[2];
const integerNumber = parseInt(firstArgument);

if (!isNaN(integerNumber)) {
  console.log(`My number: ${integerNumber}`);
} else {
  console.log('Not a number');
}
