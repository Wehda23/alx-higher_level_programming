#!/usr/bin/node
const [, , ...argv] = process.argv;

if (argv.length < 2) {
  console.log(0);
} else {
  let stack = [];

  for (let i = 0; i < argv.length; i++) {
    if (stack.length < 2) {
      stack = [parseInt(argv[i]), ...stack];
    } else {
      if (stack[0] < parseInt(argv[i])) {
        stack[0] = parseInt(argv[i]);
      }
    }

    if (stack[0] > stack[1]) {
      swap(stack);
    }
  }

  if (stack[0] > stack[1]) {
    swap(stack);
  }
  console.log(stack[0]);
}

function swap (stack) {
  const temp = stack[0];
  stack[0] = stack[1];
  stack[1] = temp;
}
