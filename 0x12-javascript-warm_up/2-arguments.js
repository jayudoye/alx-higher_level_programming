#!/usr/bin/node

const argumentNum = process.argv.slice(2);

if (argumentNum.length === 0) {
  console.log('No argument');
} else if (argumentNum.length === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
