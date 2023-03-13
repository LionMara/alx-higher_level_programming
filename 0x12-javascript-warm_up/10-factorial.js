#!/usr/bin/node

function factorial(b) {
    return b * factorial(b-1);
}

let x = parseInt(process.argv[2]);
console.log(factorial(x));
