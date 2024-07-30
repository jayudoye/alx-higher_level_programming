#!/usr/bin/node

const fs = require('fs');

const path = process.argv.slice(2)[0];

fs.readFile(path, 'utf8', function (error, text) {
	if (error) {
		console.log(error);
	} else {
		console.log(text);
	}
});
