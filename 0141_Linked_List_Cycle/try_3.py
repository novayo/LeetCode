# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # Tortoise and the Hare
        '''
        龜兔賽跑 找出cycle
        '''
        
        # 沒有 或 只有一個，不討論的話hare會有問題
        if head == None or head.next == None:
            return False
        
        tortoise = head
        hare = head
        
        while hare and hare.next:
            tortoise = tortoise.next
            hare = hare.next.next
            
            if tortoise == hare:
                return True
        return False
