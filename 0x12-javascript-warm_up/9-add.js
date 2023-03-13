#!/usr/bin/node

function add (a, b) {
  return a + b;
}
const argvTwo = parseInt(process.argv[2]);
const argvThree = parseInt(process.argv[3]);

console.log(add(argvTwo, argvThree));
