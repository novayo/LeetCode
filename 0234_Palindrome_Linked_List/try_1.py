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
        tmpnewHead = newHead = ListNode(0)
        
        cur = head
        pre = None
        
        while cur != None:
            tmpnewHead.next = ListNode(cur.val)
            tmpnewHead = tmpnewHead.next
            
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        
        newHead = newHead.next
        while pre != None:
            if pre.val == newHead.val:
                pre = pre.next
                newHead = newHead.next
            else:
                return False
        return True
