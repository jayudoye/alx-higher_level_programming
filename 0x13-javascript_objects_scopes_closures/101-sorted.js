#!/usr/bin/node
const { dict } = require('./101-data');

const userIdsByOccurrence = {};

for (const userId in dict) {
  const occurrences = dict[userId];

  if (occurrences in userIdsByOccurrence) {
    userIdsByOccurrence[occurrences].push(userId);
  } else {
    userIdsByOccurrence[occurrences] = [userId];
  }
}

console.log(userIdsByOccurrence);
