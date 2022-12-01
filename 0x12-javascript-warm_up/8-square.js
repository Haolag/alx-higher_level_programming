#!/usr/bin/node
const args = parseInt(process.argv[2], 10);
const myVar = 'X';

if (isNaN(args)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < args; i++) {
    console.log(myVar.repeat(args));
  }
}
