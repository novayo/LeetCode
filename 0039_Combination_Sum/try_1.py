class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans = set()
        def recr(index, cur_list, cur_sum):
            nonlocal ans
            
            if cur_sum > target:
                return
            elif cur_sum == target:
                ans.add(tuple(cur_list))
                return
            
            for i in range(index, len(candidates)):
                recr(i, cur_list + [candidates[i]], cur_sum + candidates[i])
        
        recr(0, [], 0)
        return ans
