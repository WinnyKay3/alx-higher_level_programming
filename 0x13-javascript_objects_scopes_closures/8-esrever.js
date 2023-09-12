#!/usr/bin/node

exports.esrever = function (list) {
  let myVar = '';

  for (let k = 0; k < list.length / 2; k++) {
    myVar = list[k];
    list[k] = list[list.length - k - 1];
    list[list.length - k - 1] = myVar;
  }
  return list;
};
