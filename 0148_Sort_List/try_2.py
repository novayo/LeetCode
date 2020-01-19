# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        
        _list = []
        while head:
            _list.append(head.val)
            head = head.next
        
        _list = self.quicksort(_list)
        ans = tmp = ListNode(_list[0])
        for i in _list[1:]:
            tmp.next = ListNode(i)
            tmp = tmp.next
            
        return ans
        
    def quicksort(self, _list):
        if len(_list) < 2:
            return _list
        else:
            pivot, equal, less, greater = _list[0], 1, [], []
            for i in _list[1:]:
                if i < pivot:
                    less.append(i)
                elif i > pivot:
                    greater.append(i)
                else:
                    equal += 1
            return self.quicksort(less) + [pivot] * equal + self.quicksort(greater)
