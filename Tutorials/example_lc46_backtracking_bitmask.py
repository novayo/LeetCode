class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        
        def backtracking(curList, bitmask):
            nonlocal ans
            if bitmask + 1 == (1 << n):
                ans.append(curList.copy())
                return
            
            for i in range(n):
                if bitmask & (1 << i) != 0:
                    continue
                
                backtracking(curList + [nums[i]], bitmask | (1 << i))
        
        backtracking([], 0)
        return ans
            
