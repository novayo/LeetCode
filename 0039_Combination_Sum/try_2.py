class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)

        ans = []
        candidates.sort(reverse=True)
        def recr(idx, curSum, curList):
            nonlocal ans
            
            if curSum == target:
                ans.append(curList.copy())
                return
            elif curSum > target:
                return
            
            for i in range(idx, n):
                recr(i, curSum + candidates[i], curList + [candidates[i]])
        
        recr(0, 0, [])
        return ans
