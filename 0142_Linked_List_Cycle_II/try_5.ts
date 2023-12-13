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

function detectCycle(head: ListNode | null): ListNode | null {
    /*
        * use set: O(n) / O(n) - where n is the number of nodes in the linked list
        * change Marked value: O(n) / O(1)
        * Tortoise and Hare: O(n) / O(1)
    */
    let hare = head, tortoise = head;
    
    // 走直到相遇
    while (hare && hare.next) {
        hare = hare.next.next;
        tortoise = tortoise.next;
        
        if (hare === tortoise) {
            break;
        }
    }
    
    // 如果沒cycle
    if (!(hare && hare.next)) {
        return null;
    }
    
    // 再跑一次，hare速度=1，直到相遇
    hare = head;
    while (hare !== tortoise) {
        hare = hare.next;
        tortoise = tortoise.next;
    }
    
    return hare;
};
