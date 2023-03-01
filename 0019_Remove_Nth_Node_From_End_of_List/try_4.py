# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # 計算長度
        total_len = 0
        ptr = head
        while ptr is not None:
            ptr = ptr.next
            total_len += 1
        
        # 刪除目前的頭
        if n == total_len:
            head = head.next
        else:
            # 往前
            ptr = head
            for _ in range(total_len-n-1):
                ptr = ptr.next
            
            # 做刪除
            ptr.next = ptr.next.next
        return head
