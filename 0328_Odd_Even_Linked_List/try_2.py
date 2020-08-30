# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # in-place
        '''
        一個去紀錄目前奇數的最右邊，之後找到下一個奇數就從這裡插入
        一個去往後掃
        '''
        # 去除0或1個的情況
        if not head or not head.next:
            return head
        
        left = head
        right = head.next
        while right and right.next:
            tmp = right.next
            right.next = right.next.next
            tmp.next = left.next
            left.next = tmp
            right = right.next
            left = left.next
        return head
