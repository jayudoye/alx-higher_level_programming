#!/usr/bin/node
const fs = require('fs');

if (process.argv.length !== 5) {
  console.log('Usage: ./concatFiles.js <file1> <file2> <destination>');
  process.exit(1);
}

const file1Path = process.argv[2];
const file2Path = process.argv[3];
const destinationPath = process.argv[4];

fs.readFile(file1Path, 'utf8', (err, file1Content) => {
  if (err) {
    console.error(`Error reading ${file1Path}: ${err.message}`);
    process.exit(1);
  }

  fs.readFile(file2Path, 'utf8', (err, file2Content) => {
    if (err) {
      console.error(`Error reading ${file2Path}: ${err.message}`);
      process.exit(1);
    }

    const concatenatedContent = file1Content + file2Content;

    fs.writeFile(destinationPath, concatenatedContent, 'utf8', (err) => {
      if (err) {
        console.error(`Error writing to ${destinationPath}: ${err.message}`);
        process.exit(1);
      }
    });
  });
});
