class Solution:
    def tilingRectangle(self, a: int, b: int) -> int:
        if b > a:
            a, b = b, a
        
        ans = float('inf')
        arr = [0] * a
        
        def dfs(trial):
            nonlocal ans
            
            if trial > ans:
                return
            
            if all([val == b for val in arr]):
                ans = min(ans, trial)
                return
            
            # find start point
            x = cur_y = b
            for i in range(a):
                if arr[i] < cur_y:
                    cur_y = arr[i]
                    x = i
            y = arr[x]
            
            # try all possibilities
            k = min(b-y, a-x)
            while k > 0 and y != arr[x+k-1]:
                k -= 1
            
            while k > 0:
                # inc k for range k
                for i in range(k):
                    arr[x+i] += k
                
                dfs(trial+1)
                
                # backtrack
                for i in range(k):
                    arr[x+i] -= k
                
                k -= 1
        
        dfs(0)
        return ans