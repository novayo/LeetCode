class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        max_stack = [] # (temp. index)
        
        for i, t in enumerate(temperatures):
            while max_stack and max_stack[-1][0] < t:
                _t, _i = max_stack.pop()
                ans[_i] = i-_i
            max_stack.append((t, i))
        
        return ans