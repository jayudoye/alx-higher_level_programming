#!/usr/bin/node
exports.esrever = function (list) {
  // Initialize an empty array to store the reversed elements
  const reversedList = [];

  // Iterate through the original list in reverse order
  for (let i = list.length - 1; i >= 0; i--) {
    // Add each element to the reversedList
    reversedList.push(list[i]);
  }

  // Return the reversed list
  return reversedList;
};
