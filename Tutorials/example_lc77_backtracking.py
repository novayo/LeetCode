class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        
        def recr(curList, startN, choose):
            nonlocal ans
            if choose == k:
                ans.append(curList.copy())
                return
            
            for i in range(startN, n+1):
                recr(curList + [i], i+1, choose + 1)
        
        recr([], 1, 0)
        return ans
