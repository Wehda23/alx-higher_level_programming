#!/user/bin/node
// Script that rights string to a file
//dependencies
const fs = require('fs');

// Grab the file name and string
const file = process.argv[2];
const string = process.argv[3];

// Write the string to the file
try {
    fs.writeFileSync(file, string, 'utf-8');
} catch (error) {
    console.log(error);
}