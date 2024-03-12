#!/usr/bin/node

const fs = require("fs");

// Check if correct number of arguments are provided
if (process.argv.length !== 5) {
  console.error("Usage: ./102-concat.js <file1> <file2> <destination>");
  process.exit(1);
}

// Get file paths from command line arguments
const [, , file1, file2, destination] = process.argv;

// Read content of file1
fs.readFile(file1, "utf8", (err, data1) => {
  if (err) {
    console.error(`Error reading ${file1}: ${err.message}`);
    process.exit(1);
  }

  // Read content of file2
  fs.readFile(file2, "utf8", (err, data2) => {
    if (err) {
      console.error(`Error reading ${file2}: ${err.message}`);
      process.exit(1);
    }

    // Concatenate contents of file1 and file2
    const concatenatedContent = `${data1}\n${data2}\n`;

    // Write concatenated content to destination file
    fs.writeFile(destination, concatenatedContent, (err) => {
      if (err) {
        console.error(`Error writing to ${destination}: ${err.message}`);
        process.exit(1);
      }
    });
  });
});
