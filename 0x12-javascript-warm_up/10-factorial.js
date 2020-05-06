#!/usr/bin/node

const num = process.argv[2];
function factorial (num) {
  let i = 1;
  let ans = 1;
  if (num) {
    while (i <= num) {
      ans *= i;
      i++;
    }
  } else {
    return (1);
  }
  return (ans);
}
console.log(factorial(num));
