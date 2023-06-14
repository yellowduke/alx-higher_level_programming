#!/usr/bin/node
//auth:yellowduke
const firstNum = Number(process.argv[2]);
const secondNum = Number(process.argv[3]);


add(firstNum, secondNum);

function add (a, b) {
  console.log(a + b);
}
