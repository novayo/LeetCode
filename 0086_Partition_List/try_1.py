# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        def print_():
            tmp = lower_pre_head.next
            while tmp:
                print(tmp.val, end='->')
                tmp = tmp.next
            print('')
            
        
        lower_pre_head = ListNode(0, head)
        lower_ptr = lower_pre_head
        higher_head = None
        higher_ptr = None
        
        preNode = lower_pre_head
        curNode = preNode.next
        while curNode:
            if curNode.val < x:
                if preNode == lower_ptr:
                    preNode = preNode.next
                    curNode = curNode.next
                else:
                    old_ptr_next = lower_ptr.next
                    preNode.next = curNode.next
                    lower_ptr.next = curNode
                    curNode.next = old_ptr_next
                    curNode = preNode.next
                lower_ptr = lower_ptr.next

            else:
                if higher_head == None:
                    higher_head = curNode
                    higher_ptr = higher_head
                    preNode = preNode.next
                    curNode = curNode.next
                    continue
                elif preNode == higher_ptr:
                    preNode = preNode.next
                    curNode = curNode.next
                else:
                    old_ptr_next = higher_ptr.next
                    preNode.next = curNode.next
                    higher_ptr.next = curNode
                    curNode.next = old_ptr_next
                    curNode = preNode.next
                higher_ptr = higher_ptr.next
        return lower_pre_head.next