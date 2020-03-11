# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # time complexity: O(n^2)
        ans = tmp = ListNode(0)
        
        while True:
            tmpMin = [-1, float('inf')]
            for index, l in enumerate(lists):
                if l and l.val < tmpMin[1]:
                    tmpMin = [index, l.val]
            
            if tmpMin[0] == -1: break
            
            lists[tmpMin[0]] = lists[tmpMin[0]].next
            tmp.next = ListNode(tmpMin[1])
            tmp = tmp.next
        
        return ans.next
