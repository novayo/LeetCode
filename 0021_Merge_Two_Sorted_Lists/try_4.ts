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

function mergeTwoLists(list1: ListNode | null, list2: ListNode | null): ListNode | null {
    const dummy: ListNode = new ListNode(-1);

    let tmp: ListNode | null = dummy;
    while (list1 && list2) {
        if (list1.val >= list2.val) {
            tmp.next = list2;
            list2 = list2.next;
        } else {
            tmp.next = list1;
            list1 = list1.next;
        }
        tmp = tmp.next;
    }

    if (list1) {
        tmp.next = list1;
    }
    if (list2) {
        tmp.next = list2;
    }

    return dummy.next;
};
