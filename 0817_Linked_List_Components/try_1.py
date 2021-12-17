# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        ans = 0
        nums_set = set(nums)
        isConnected = False
        
        tmp = head
        while tmp:
            if tmp.val in nums_set:
                if not isConnected:
                    isConnected = True
                    ans += 1
            else:
                isConnected = False
            
            tmp = tmp.next
        
        return ans
