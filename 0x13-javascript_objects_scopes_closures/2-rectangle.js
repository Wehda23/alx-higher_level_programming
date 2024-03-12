#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    this.setWidth(w > 0 && h > 0 ? w : undefined);
    this.setHeight(h > 0 && w > 0 ? h : undefined);
  }

  setWidth (width) {
    this.width = width;
  }

  setHeight (height) {
    this.height = height;
  }
}

module.exports = Rectangle;
