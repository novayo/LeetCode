class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        n = len(properties)
        properties.sort(key=lambda x: (x[0], -x[1]))
        ans = 0
        
        stack = []
        for x, y in properties:
            while stack and stack[-1][0] < x and stack[-1][1] < y:
                stack.pop()
                ans += 1
            stack.append([x, y])
        return ans
