#!/usr/bin/node

const computeFactorial = (n) => {
  if (isNaN(n)) {
    return 1; // Factorial of NaN is 1
  }

  n = parseInt(n);

  if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * computeFactorial(n - 1);
  }
};

const input = process.argv[2];

const result = computeFactorial(input);
console.log(result);
