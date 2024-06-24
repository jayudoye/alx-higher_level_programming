#!/usr/bin/node

const myObject = {
  type: 'object',
  value: 12
};

console.log(myObject);

// Add the increment function to the myObject
myObject.incr = function () {
  this.value++;
};

myObject.incr();
console.log(myObject);

myObject.incr();
console.log(myObject);

myObject.incr();
console.log(myObject);
