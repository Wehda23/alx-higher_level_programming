#!/usr/bin/node

class Square extends require('./5-square') {
  constructor (size) {
    super(size, size);
  }

  charPrint (character) {
    const symbole = character || 'X';

    for (let i = 0; i < this.height; i++) {
      console.log(symbole.repeat(this.width));
    }
  }
}

module.exports = Square;
