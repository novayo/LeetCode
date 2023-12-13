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
    // O(n) / O(n) - where n is number of nodes in the linkedlist
    if (head === null) {
        return null;
    }
    
    let tail = null;
    function recr(node: ListNode | null) {
        if (node.next === null) {
            tail = node;
            return node;
        }
        
        recr(node.next).next = node;
        node.next = null;
        return node;
    }
    
    recr(head);
    return tail;
};
