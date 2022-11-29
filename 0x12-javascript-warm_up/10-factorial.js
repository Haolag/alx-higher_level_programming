#!/usr/bin/node

const args = parseInt(process.argv[2], 10);
function factorial (num) {
  if (isNaN(num) || num === 0) {
    return (1);
  }
  return (num * factorial(num - 1));
}
console.log(factorial(args));
