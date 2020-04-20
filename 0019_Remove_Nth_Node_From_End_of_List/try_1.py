# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 一開始讓slow跟fast相差n格，之後一起往後走，等走到底
        # slow的前面就是要刪掉的，所以slow.next = slow.next.next
        
        slow = fast = head
        for _ in range(n, 0, -1):
            fast = fast.next
        
        if fast == None: # n等於整個linked list的長度，因此直接捨棄頭即可
            return slow.next

        fast = fast.next
        
        while fast:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        return head
