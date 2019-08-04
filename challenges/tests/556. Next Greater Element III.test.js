const { nextGreaterElement } = require("../556. Next Greater Element III.js");

describe("Main function", () => {
  test("non trivial permutation", () => {
    expect(nextGreaterElement(527641)).toBe(541267);
  });
  test("no permutaion", () => {
    expect(nextGreaterElement(765431)).toBe(-1);
  });
  test("permutaion is above 32 bit", () => {
    expect(nextGreaterElement(2147483647)).toBe(-1);
  });
  test("number is too small", () => {
    expect(nextGreaterElement(5)).toBe(-1);
  });
  test("same digits", () => {
    expect(nextGreaterElement(55555555)).toBe(-1);
  });
});
