#!/usr/bin/node
//auth:yellowduke
let num = process.argv[2];
num = Number(num);

if ((num === undefined) || isNaN(num)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${num}`);
}
