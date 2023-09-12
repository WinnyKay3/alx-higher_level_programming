#!/usr/bin/node

exports.nbOccurrences = function (list, searchElement) {
  let occur = 0;

  for (let k = 0; k < list.length; k++) {
    if (searchElement === list[k]) {
      occur++;
    }
  }
  return occur;
};
