#!/usr/bin/node

const request = require('request');

const fs = require('fs');

const url = process.argv[2];

const filePath = process.argv[3];

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode !== 200) {
    console.error('Failed to retrieve webpage content. Status code:', response.statusCode);
  } else {
    fs.writeFileSync(filePath, body, 'utf-8');
  }
});
