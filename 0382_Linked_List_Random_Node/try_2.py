# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        
    def getRandom(self) -> int:
        count = 1
        ans = 0
        head = self.head
        
        while head:
            if random.random() < 1/count:
                ans = head.val
            count += 1
            head = head.next
        return ans

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
