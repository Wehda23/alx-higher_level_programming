// Dependencies
const fs = require("fs");

// Grab Arguments and File name
const args = process.argv;
const fileName = args[2] ? args[2] : null;

try {
    // Read content of a file
    const content = fs.readFileSync(fileName, 'utf8');
    // Print the content
    console.log(content);
} catch (error) {
    // In case of error print error
    console.error(error);
}