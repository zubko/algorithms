/**
 * 39. Combination Sum
 * https://leetcode.com/problems/combination-sum/description/
 * Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.
 * The same repeated number may be chosen from candidates unlimited number of times.
 * Note:
 * All numbers (including target) will be positive integers.
 * The solution set must not contain duplicate combinations.
 */
function combinationSum(candidates, target) {
  candidates.sort((a, b) => a - b);
  var buffer = [];
  var result = [];
  search(0, target);
  return result;

  function search(startIdx, target) {
    if (target === 0) {
      return result.push(buffer.slice());
    }
    if (target < 0) {
      return;
    }
    if (startIdx === candidates.length) {
      return;
    }
    buffer.push(candidates[startIdx]);
    search(startIdx, target - candidates[startIdx]);
    buffer.pop();
    search(startIdx + 1, target);
  }
}

module.exports = { combinationSum };
