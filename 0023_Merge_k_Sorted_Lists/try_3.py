# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        '''
        用heap去排序，由於插入是O(logn)，因此總複雜度為O(nlogn)
        '''
        root = tmp = ListNode(-1)
        
        heap = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))
        
        while heap:
            val, index = heapq.heappop(heap)
            
            tmp.next = ListNode(val)
            tmp = tmp.next
            lists[index] = lists[index].next
            
            if lists[index]:
                heapq.heappush(heap, (lists[index].val, index))
                
        return root.next
