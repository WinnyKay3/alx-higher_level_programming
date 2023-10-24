#!/usr/bin/node

const fs = require('fs');

// get filename from arguments
const fileName = process.argv[2];

if (!fileName) {
   console.error('Usage: .0-readme.js <fileName>');
   process.exit(1);
 }

// read content of the file in utf-8 encoding
fs.readFile(fileName, 'utf-8', (err, data) => {
  if (err) {

     console.error(err);
   } else {
     // prints the contents of file
     console.log(data);
   }
});
