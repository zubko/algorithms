/**
 * 556. Next Greater Element III
 * https://leetcode.com/problems/next-greater-element-iii/description/
 */

const MAX_INT_32 = 2147483647;

/**
 * Entry point
 * @param {number} n
 * @return {number}
 */
const nextGreaterElement = function(n) {
  if (n < 12) {
    return -1;
  }
  const digits = _numberToDigits(n);
  if (!_permutateNext(digits)) {
    return -1;
  }
  const result = _digitsToNumber(digits);
  return result <= MAX_INT_32 ? result : -1;
};

const _permutateNext = function(digits) {
  // check on which index the descending sort breaks
  let lastSortedI = -1;
  for (let i = digits.length - 1; i >= 1; i--) {
    if (digits[i] > digits[i - 1]) {
      lastSortedI = i;
      break;
    }
  }
  if (lastSortedI == -1) {
    return false;
  }
  // push the next bigger number instead (sub-sequence is sorted)
  // sort the new subsequence ascending
  for (let i = digits.length - 1; i >= lastSortedI; i--) {
    if (digits[i] > digits[lastSortedI - 1]) {
      _arraySwapElements(digits, i, lastSortedI - 1);
      const newSorted = digits.splice(lastSortedI).sort((a, b) => a > b);
      digits.push(...newSorted);
      break;
    }
  }
  return true;
};

const _arraySwapElements = function(array, i, j) {
  const temp = array[i];
  array[i] = array[j];
  array[j] = temp;
};

const _numberToDigits = function(n) {
  const digits = [];
  let i = 0;
  while (n > 0) {
    digits.push(n % 10);
    n = Math.floor(n / 10);
  }
  return digits.reverse();
};

const _digitsToNumber = function(digits) {
  let n = 0;
  let m = 1;
  for (let i = digits.length - 1; i >= 0; i--) {
    n += digits[i] * m;
    m *= 10;
  }
  return n;
};
