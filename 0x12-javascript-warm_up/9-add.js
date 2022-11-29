#!/usr/bin/node

const arg2 = parseInt(process.argv[2], 10);
const arg3 = parseInt(process.argv[3], 10);

function add (a, b) {
  return a + b;
}
console.log(add(arg2, arg3));
