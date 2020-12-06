# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        root = tmp = ListNode(-1)
        valid = set()
        for i in range(len(lists)):
            if lists[i]:
                valid.add(i)
        
        while valid:
            # find min
            minValue = list(valid)[0]
            for value in valid:
                if lists[value].val < lists[minValue].val:
                    minValue = value
            
            # create Node
            tmp.next = ListNode(lists[minValue].val)
            tmp = tmp.next
            lists[minValue] = lists[minValue].next
            
            if lists[minValue] == None:
                valid.remove(minValue)
                
        return root.next
