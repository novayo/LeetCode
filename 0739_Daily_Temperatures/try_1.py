class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        ans = [0] * len(T)
        
        stack = [] # [value, index]
        for i, v in enumerate(T):
            while stack:
                if v > stack[-1][0]:
                    _, prei = stack.pop()
                    ans[prei] = i - prei
                else:
                    break
            
            stack.append([v, i])
        
        return ans