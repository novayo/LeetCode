class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        # 用dp去記錄哪些點有跑過了
        # 用dfs去爆出所有點
        
        dp = [False] * len(arr)
        ret = False
        
        def dfs(index):
            nonlocal ret
            if ret:
                return
            if index < 0 or index >= len(arr) or dp[index]:
                return
            
            if arr[index] == 0:
                ret = True
                return
            
            dp[index] = True
            dfs(index-arr[index])
            dfs(index+arr[index])
        
        dfs(start)
        return ret
