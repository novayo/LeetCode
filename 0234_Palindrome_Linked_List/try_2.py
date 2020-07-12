# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # reverse and compare
        # O(n) O(n)
        '''
        直接拷貝一份，並把原本的給reverse，再去比較即可
        '''
        tmp = []
        while head != None:
            tmp.append(head.val)
            head = head.next
        return tmp == tmp[::-1]
