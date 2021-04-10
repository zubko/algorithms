const {
  prisonAfterNDays,
  isEqualArrays,
  advanceOneDay
} = require("../957. Prison Cells After N Days.js");

describe("main function", () => {
  test("example 1 from leetcode", () => {
    const input = [0, 1, 0, 1, 1, 0, 0, 1];
    const days = 7;
    const output = [0, 0, 1, 1, 0, 0, 0, 0];
    expect(prisonAfterNDays(input, days)).toEqual(output);
  });

  test("example 2 from leetcode", () => {
    const input = [1, 0, 0, 1, 0, 0, 1, 0];
    const days = 1000000000;
    const output = [0, 0, 1, 1, 1, 1, 1, 0];
    expect(prisonAfterNDays(input, days)).toEqual(output);
  });

  test("when needs the day which eq the first day", () => {
    const input = [0, 1, 0, 1, 1, 0, 0, 1];
    const days = 29;
    const output = [0, 1, 1, 0, 0, 0, 0, 0];
    expect(prisonAfterNDays(input, days)).toEqual(output);
  });
});

describe("advance one day", () => {
  test("random day", () => {
    const day = [0, 1, 1, 0, 0, 1, 0, 0];
    const next = [0, 0, 0, 0, 0, 1, 0, 0];
    const out = Array(day.length);
    expect(advanceOneDay(day, out)).toEqual(next);
  });
  test("all ones", () => {
    const day = [1, 1, 1, 1, 1, 1, 1, 1];
    const next = [0, 1, 1, 1, 1, 1, 1, 0];
    const out = Array(day.length);
    expect(advanceOneDay(day, out)).toEqual(next);
  });
  test("all zeros", () => {
    const day = [0, 0, 0, 0, 0, 0, 0, 0];
    const next = [0, 1, 1, 1, 1, 1, 1, 0];
    const out = Array(day.length);
    expect(advanceOneDay(day, out)).toEqual(next);
  });
});

describe("equal arrays", () => {
  test("when different length", () => {
    const a = [0, 1, 0, 1, 1];
    const b = [0, 1, 0, 1, 1, 0, 0, 0];
    expect(isEqualArrays(a, b)).toBe(false);
  });
  test("when arrays are not equal", () => {
    const a = [0, 1, 0, 1, 1, 0, 0, 1];
    const b = [0, 0, 1, 1, 0, 0, 0, 0];
    expect(isEqualArrays(a, b)).toBe(false);
  });
  test("when arrays are equal", () => {
    const a = [0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1];
    const b = [0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1];
    expect(isEqualArrays(a, b)).toBe(true);
  });
});
