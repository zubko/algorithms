/**
 * 957. Prison Cells After N Days
 * https://leetcode.com/problems/prison-cells-after-n-days/
 *
 * There are 8 prison cells in a row, and each cell is either occupied or vacant.
 *
 * Each day, whether the cell is occupied or vacant changes according to the following rules:
 *
 * If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
 * Otherwise, it becomes vacant.
 * (Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.)
 *
 * We describe the current state of the prison in the following way: cells[i] == 1 if the i-th cell is occupied, else cells[i] == 0.
 *
 * Given the initial state of the prison, return the state of the prison after N days (and N such changes described above.)
 *
 */

/**
 * @param {number[]} cells
 * @param {number} N
 * @return {number[]}
 */
const prisonAfterNDays = function(cells, N) {
  let periodOfEquality = 0;
  let tempCells = Array(cells.length);
  advanceOneDay(cells, tempCells);
  [cells, tempCells] = [tempCells, cells];
  let day1Cells = [...cells];
  for (let day = 2; day <= N; day += 1) {
    advanceOneDay(cells, tempCells);
    [cells, tempCells] = [tempCells, cells];
    if (!periodOfEquality && isEqualArrays(cells, day1Cells)) {
      periodOfEquality = day - 1;
      const daysLeft = N - day;
      const jumpTimes = Math.floor(daysLeft / periodOfEquality);
      day += jumpTimes * periodOfEquality;
    }
  }
  return cells;
};

function advanceOneDay(cells, outCells) {
  outCells[0] = 0;
  outCells[cells.length - 1] = 0;
  for (let i = 1; i < cells.length - 1; i += 1) {
    outCells[i] = cells[i - 1] === cells[i + 1] ? 1 : 0;
  }
  return outCells;
}

function isEqualArrays(a, b) {
  if (a.length !== b.length) return false;
  for (let i = 0; i < a.length; i++) {
    if (a[i] !== b[i]) return false;
  }
  return true;
}

module.exports = { prisonAfterNDays, isEqualArrays, advanceOneDay };
