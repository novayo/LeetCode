class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        flag = True
        tortoise = nums[0]
        hare = nums[0]
        
        # meet first
        while flag or hare != tortoise:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            flag = False
        
        # hare start from nums[0] => move one step when meet tortoise again
        hare = nums[0]
        while hare != tortoise:
            tortoise = nums[tortoise]
            hare = nums[hare]
        
        return hare
