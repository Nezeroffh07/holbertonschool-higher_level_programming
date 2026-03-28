#!/usr/bin/node
const myInt = parseInt(process.argv[2]);

if (isNaN(myInt)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + myInt);
}
