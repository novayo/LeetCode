# time complexity: O(nlogn)
# space complexity: O(1)
# 
# quicksort
# TLE
# 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def printf(node):
            tmp = node
            while tmp:
                print(tmp.val, end='->')
                tmp = tmp.next
            print()
        
        tmp = ListNode(0)
        tmp.next = head
        
        def recr(left_node, end_node):
            if left_node.next == end_node:
                return
            pivot = left_node.next
            
            pre = pivot
            cur = pre.next
            while cur:
                if cur == end_node:
                    break
                    
                if cur.val < pivot.val:
                    pre.next = cur.next
                    cur.next = left_node.next
                    left_node.next = cur
                    cur = pre.next
                elif cur.val == pivot.val:
                    pre.next = cur.next
                    cur.next = pivot.next
                    pivot.next = cur
                    pivot = pivot.next
                else:
                    cur = cur.next
                    pre = pre.next
            
            recr(left_node, pivot)
            recr(pivot, end_node)
            
        recr(tmp, None)
        return tmp.next