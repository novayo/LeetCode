# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return None
        
        # O(n) O(1)
        hare = head
        tortoise = head
        
        while hare and hare.next:
            hare = hare.next.next
            tortoise = tortoise.next
            
            # 第一次相遇
            if hare == tortoise:
                break
        
        if hare != tortoise:
            return None
        
        tortoise2 = head
        while tortoise != tortoise2:
            tortoise = tortoise.next
            tortoise2 = tortoise2.next
        
        return tortoise
        
        
#         '''
#         found = set()
        
#         found.add(node3)
#         found.add(node2)
#         found.add(node0)
#         found.add(node-4)
#         '''
#         # time complexity: O(n)
#         # space complexity: O(n)
#         found = set()
        
        
#         node = head
#         while node:
#             if node in found:
#                 return node
#             else:
#                 found.add(node)
#             node = node.next
        
#         return None