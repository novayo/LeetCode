# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # iteratively
        '''
        直接把每個都往前指，就可以直接reverse了
        
        1->2->3->4
        pre(null) cur(1) tmp(2)
        讓cur指向pre，把pre更新到cur，cur再到tmp
        pre(1) cur(2) tmp(3)
        '''
        
        cur = head
        pre = None
        
        while cur != None:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre
