class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (x[0], -x[1]))
        
        ans = 0
        stack = []
        for a, b in properties:
            while stack and stack[-1][0] < a and stack[-1][1] < b:
                stack.pop()
                ans += 1
            stack.append((a, b))
        
        return ans
