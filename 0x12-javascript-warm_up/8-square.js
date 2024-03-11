#!/usr/bin/node
const size = parseInt(process.argv[2]);

if (isNaN(size)) {
  console.log('Missing size');
} else {
  const symbole = 'X';
  let row = '';
  for (let j = 0; j < size; j++) {
    row += symbole;
  }
  for (let i = 0; i < size; i++) {
    console.log(row);
  }
}
