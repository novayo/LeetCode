class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def recr(idx, cur_sum, cur_list):
            nonlocal ans
            if cur_sum > target:
                return
            if cur_sum == target:
                ans.append(cur_list[:])
                return
            
            if idx >= n:
                return
            
            for i in range(idx, n):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                recr(i+1, cur_sum + candidates[i], cur_list + [candidates[i]])
        
        n = len(candidates)
        ans = []
        candidates.sort()
        recr(0, 0, [])
        return ans