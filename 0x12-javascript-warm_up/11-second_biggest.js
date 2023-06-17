#!/usr/bin/node
function secondLargest (a) {
  if (a.length < 4) {
    return 0;
  } else {
    let max = -Infinity;
    let secondMax = -Infinity;

    for (let i = 0; i < a.length; i++) {
      const intValue = parseInt(a[i]);
      if (intValue > max) {
        secondMax = max;
        max = intValue;
      } else if (intValue > secondMax && intValue < max) {
        secondMax = intValue;
      }
    }
    return secondMax;
  }
}

const numbers = process.argv;
console.log(secondLargest(numbers));
