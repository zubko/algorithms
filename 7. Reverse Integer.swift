/**
 * 7. Reverse Integer
 * https://leetcode.com/problems/reverse-integer/description/
 *
 * Xcode Playground code
 * Swift 4.1
 * /

import Foundation

func reverse(_ x: Int) -> Int {
  var number: Int32 = Int32(x);
  var reversed: Int32 = 0;
  while (number != 0) {
    let digit: Int32 = number % 10
    var (r, overflow) = reversed.multipliedReportingOverflow(by: 10)
    if (overflow) {
      return 0
    }
    (r, overflow) = r.addingReportingOverflow(digit)
    if (overflow) {
      return 0
    }
    reversed = r
    number /= 10
  }
  return Int(reversed)
}

import XCTest
class Tests: XCTestCase {
  func testZero() {
    XCTAssertEqual(reverse(0), 1);
  }
  func testGeneral() {
    XCTAssertEqual(reverse(987654321), 123456789);
  }
  func testZeroEnding() {
    XCTAssertEqual(reverse(1000), 1);
  }
  func testNegative() {
    XCTAssertEqual(reverse(-12345), -54321); 
  }
  func testExtremes() {
    XCTAssertEqual(reverse(2147483647), 0);
    XCTAssertEqual(reverse(-2147483648), 0);
  }
  func testPerformance() {
    self.measure {
      for i in 12345678..<12345778 {
        reverse(i)
      }
    }
  }
}

Tests.defaultTestSuite.run()
