#!/usr/bin/node

const num = parseInt(process.argv[2]);

if (!process.argv[2]) {
  console.log('Not a number');
} else if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${num}`);
}
