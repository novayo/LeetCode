class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        '''
        a,b,c,d,e,f,g,h,i,j
            1
                2
                  5
                    6
                      7
                          11
            ^.    ^
                |   |
                      k    k 
        target = 4
        記錄說：某個index往前，最小的長度是...
        '''
        n = len(arr)
        prefix = [0] * n
        cur = 0
        for i in range(n):
            cur += arr[i]
            prefix[i] = cur
        
        
        # Get answer
        ans = float('inf')
        dp = [float('inf')] * n
        cache = {0: -1}
        
        for i in range(n):
            comp = prefix[i] - target
            
            # if hit
            if comp in cache:
                # 取得目前答案
                j = cache[comp]
                current_answer = i - j
                
                # 更新answer
                ans = min(ans, current_answer + dp[j])
                
                # 更新dp
                if i == 0:
                    dp[i] = current_answer
                else:
                    dp[i] = min(dp[i-1], current_answer)
            else:
                dp[i] = dp[i-1]
                
            cache[prefix[i]] = i
        
        return ans if ans < float('inf') else -1

