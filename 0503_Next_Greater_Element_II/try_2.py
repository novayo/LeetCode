class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []
        ans = [-1] * n
        for i in range(2*n):
            val = nums[i%n]
            
            while stack and stack[-1][1] < val:
                idx, _ = stack.pop()

                ans[idx%n] = val
            
            stack.append((i, val))
        
        return ans

