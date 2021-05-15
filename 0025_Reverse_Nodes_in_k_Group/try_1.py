# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 1:
            return head
        
        newhead = ListNode(-1)
        newhead.next = head
        prehead = newhead
        
        run_once = True
        pre = head
        cur = pre.next
        count = 1
        while cur:
            pre.next = cur.next
            cur.next = head
            prehead.next = head = cur
            cur = pre.next
            count += 1
            
            if count >= k:
                prehead = pre
                head = cur
                pre = pre.next
                cur = cur.next if cur else None
                count = 1
            
            # 如果跑到底了count沒有歸位，則從head再跑一次，reverse回來
            if run_once and not cur and count > 1:
                pre = head
                cur = pre.next
                count = 1
                run_once = False

        return newhead.next