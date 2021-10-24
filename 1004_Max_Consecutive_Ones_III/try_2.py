class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # monotonic queue
        dq = collections.deque()
        
        i = 0
        cur_zero = 0
        while i < len(nums) and cur_zero < k:
            dq.append(nums[i])
            if nums[i] == 0:
                cur_zero += 1
            i += 1
        
        ans = len(dq)
        while i < len(nums):
            dq.append(nums[i])
            if nums[i] == 0:
                while dq[0] != 0:
                    dq.popleft()
                dq.popleft()
            ans = max(ans, len(dq))
            i += 1
        
        return ans