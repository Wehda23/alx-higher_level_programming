#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    this.setWidth(w && h ? w : undefined);
    this.setHeight(h && w ? h : undefined);
  }

  setWidth (width) {
    this.width = width;
  }

  setHeight (height) {
    this.height = height;
  }
}

module.exports = Rectangle;
