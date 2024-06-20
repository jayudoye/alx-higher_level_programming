#!/usr/bin/node

const argumentNum = process.argv.length - 2;

if (argumentNum === 0) {
	console.log('No argument');
} else if (argumentNum === 1) {
	console.log('Argument found');
} else {
	console.log('Arguments found');
}
