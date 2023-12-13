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

function removeNthFromEnd(head: ListNode | null, n: number): ListNode | null {
    // O(N) / O(1) - where N is the number of nodes in the list
    let ptr = head, tail = head;
    
    // 創建dummy node指向head
    let dummy = new ListNode(-1, head);
    let pre_ptr = dummy;
    
    // tail 移動n-1格
    for (let i = 0; i < n-1; i++) {
        tail = tail.next;
    }
    
    // 所有ptr一起移動直到tail走到底
    while (tail.next !== null) {
        ptr = ptr.next;
        pre_ptr = pre_ptr.next;
        tail = tail.next;
    }
    
    // delete ptr
    pre_ptr.next = ptr.next
    
    return dummy.next;
};
