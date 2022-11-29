#!/usr/bin/node
function ascending (a, b) {
  return b - a;
}
const args = process.argv.length;
if (args <= 3) {
  console.log(0);
} else {
  console.log(process.argv.slice(2).sort(ascending)[1]);
}
