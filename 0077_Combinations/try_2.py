class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        ans = []
        def backtrack(list, start, ans):
            if len(list) == k:
                ans.append(list)
                return
            
            for i in range(start, n+1):
                # 如果之後的組合都不可能長度達到k，就不找了
                if len(list) + n - i + 1 < k:
                    break
                backtrack(list + [i], i+1, ans)
            
        
        backtrack([], 1, ans)
        return ans
