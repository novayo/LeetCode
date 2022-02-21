class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        
        def backtracking(cur_list, bitmask):
            nonlocal ans
            
            if bitmask == 2**n-1:
                ans.append(cur_list.copy())
                return
            
            for i in range(n):
                if bitmask & 2**i != 0:
                    continue
                
                cur_list.append(nums[i])
                bitmask += 2**i
                backtracking(cur_list, bitmask)
                cur_list.pop()
                bitmask -= 2**i
        
        backtracking([], 0)
        return ans