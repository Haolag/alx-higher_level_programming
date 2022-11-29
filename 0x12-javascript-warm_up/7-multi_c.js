#!/usr/bin/node
const args = parseInt(process.argv[2], 10);
const myVar = 'C is fun';

if (isNaN(args)) {
  console.log('Missing number of ocurrences');
} else {
  for (let i = 0; i < args; i++) {
    console.log(myVar);
  }
}
