#!/usr/bin/node
const dict = require('./101-data.js');

const usersByOccurences = {};

for (const userId in dict) {
  const occurrences = dict[userId];
  if (occurrences in usersByOccurences) {
    usersByOccurences[occurrences].push(userId);
  } else {
    usersByOccurences[occurrences] = [userId];
  }
}
console.log(usersByOccurences);
