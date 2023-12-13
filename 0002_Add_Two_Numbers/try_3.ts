/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function addTwoNumbers(l1: ListNode | null, l2: ListNode | null): ListNode | null {
    let tmp: ListNode | null = new ListNode();
    let head: ListNode | null = tmp;
    let carry: number = 0;

    while (l1 || l2 || carry) {
        if (l1) {
            carry += l1.val;
            l1 = l1.next;
        }

        if (l2) {
            carry += l2.val;
            l2 = l2.next;
        }

        tmp.next = new ListNode(carry % 10);
        tmp = tmp.next;
        carry = Math.floor(carry / 10);
    }

    return head.next;
};
