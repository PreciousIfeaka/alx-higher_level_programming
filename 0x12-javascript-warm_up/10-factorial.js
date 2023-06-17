#!/usr/bin/node
const integer = parseInt(process.argv[2]);
let factorial;

if (!isNaN(integer)) {
  factorial = integer;
  for (let i = integer - 1; i > 1; i--) {
    factorial = factorial * i;
  }
  console.log(factorial);
} else {
  factorial = 1;
  console.log(factorial);
}
