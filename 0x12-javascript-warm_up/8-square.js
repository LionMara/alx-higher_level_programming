#!/usr/bin/node

const x = process.argv[2];

if (!Number(x)) {
  console.log('Missing size');
} else {
  for (let rows = 0; rows < +x; rows++) {
    let row = '';
    for (let cols = 0; cols < +x; cols++) {
      row += 'X';
    }
    console.log(row);
  }
}
