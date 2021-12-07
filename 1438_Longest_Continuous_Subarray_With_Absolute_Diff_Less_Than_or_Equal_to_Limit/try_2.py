class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minQueue = collections.deque()
        maxQueue = collections.deque()
        
        ans = l = r = 0
        while r < len(nums):
            while minQueue and nums[minQueue[-1]] > nums[r]:
                minQueue.pop()
            
            while maxQueue and nums[maxQueue[-1]] < nums[r]:
                maxQueue.pop()
            
            minQueue.append(r)
            maxQueue.append(r)
            
            if nums[maxQueue[0]] - nums[minQueue[0]] > limit:
                l += 1
                while minQueue and minQueue[0] < l:
                    minQueue.popleft()
                while maxQueue and maxQueue[0] < l:
                    maxQueue.popleft()
            
            ans = max(ans, r-l+1)
            r += 1
            
        return ans
            
