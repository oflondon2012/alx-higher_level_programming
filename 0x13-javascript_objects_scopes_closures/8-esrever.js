#!/usr/bin/node
exports.esrever = function (list) {
  const revlist = [];
  for (let j = list.length - 1; j >= 0; j--) {
    revlist.push(list[j]);
  }
  return revlist;
};
