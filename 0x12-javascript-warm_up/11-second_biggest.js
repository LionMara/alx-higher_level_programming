#!/usr/bin/node

if (!process.argv[2] || !process.argv[3]) {
    console.log(0);
} else {
    let myArray = process.argv;
    for (let i = 2; i < myArray.length; i++) {
	console.log(myArray[i]);
    }
}
