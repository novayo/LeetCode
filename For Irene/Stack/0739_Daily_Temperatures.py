class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        min_stack = [] # (val, index)
        
        for i, t in enumerate(temperatures):
            while min_stack and min_stack[-1][0] < t:
                val, index = min_stack.pop()
                ans[index] = i - index
            
            min_stack.append((t, i))
        return ans