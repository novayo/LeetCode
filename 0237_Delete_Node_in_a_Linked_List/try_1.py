# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        
        '''
        題目給的node就是要刪除的那個點
        
        4->5->1->9
        假設node=5
        那要怎麼刪除5?
        就把5變成他的下一位1
        之後再刪除下一個1即可
        '''
        node.val = node.next.val
        node.next = node.next.next
