#!/usr/bin/node

const firstArgument = process.argv[2];
const count = parseInt(firstArgument);

if (isNaN(count)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < count; i++) {
    console.log('C is fun');
  }
}
