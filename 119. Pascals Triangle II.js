/**
 * 119. Pascal's Triangle II
 * https://leetcode.com/problems/pascals-triangle-ii/description/
 *
 * @param {number} rowIndex
 * @return {number[]}
 */
var getRow = function(rowIndex) {
  // doing only the right part of triangle
  let row = [1];
  for (let i = 2; i <= rowIndex; i++) {
    let newRow = [];
    if (i % 2 === 0) {
      newRow.push(row[0] * 2);
    }
    for (let j = 0; j < row.length - 1; j++) {
      newRow.push(row[j] + row[j + 1]);
    }
    newRow.push(1);
    row = newRow;
  }
  const copyIndex = rowIndex % 2 === 1 ? 0 : 1;
  return row
    .slice(copyIndex)
    .reverse()
    .concat(row);
};
