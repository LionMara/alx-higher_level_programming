#!/usr/bin/node

exports.esrever = function (list) {
  const emptyList = [];
  const len = list.length;

  for (let i = 0, j = len - 1; i < len; i++, j--) {
    emptyList[j] = list[i];
  }
  return emptyList;
};
