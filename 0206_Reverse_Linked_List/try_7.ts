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

function reverseList(head: ListNode | null): ListNode | null {
    if (head === null) {
        return null;
    }
    
    let dummy = new ListNode(-1, head);
    let ptr = head.next;
    
    while (ptr) {
        head.next = ptr.next;
        ptr.next = dummy.next;
        dummy.next = ptr;
        ptr = head.next;
    }
    
    return dummy.next;
};
