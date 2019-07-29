/**
 * 328. Odd Even Linked List
 * https://leetcode.com/problems/odd-even-linked-list/description/
 */

/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var oddEvenList = function(head) {
  let oddsHead = head;
  let evensHead = head && head.next;
  let oddsTail = null;
  let evensTail = null;
  let i = 0;
  while (head) {
    if (i % 2 === 0) {
      oddsTail && (oddsTail.next = head);
      oddsTail = head;
    } else {
      evensTail && (evensTail.next = head);
      evensTail = head;
    }
    head = head.next;
    i += 1;
  }
  evensTail && (evensTail.next = null);
  oddsTail && (oddsTail.next = evensHead);
  return oddsHead;
};
