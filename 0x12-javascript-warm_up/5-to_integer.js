#!/usr/bin/node

const numberEntered = process.argv[2];

if (Number(numberEntered)) {
  console.log(`My number: ${+Math.round(numberEntered)}`);
} else {
  console.log('Not a number');
}
