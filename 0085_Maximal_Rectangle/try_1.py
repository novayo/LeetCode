class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        memo = {}
        def helper(array):
            t = tuple(array)
            if t not in memo:
                ans = i = 0
                while i < len(array):
                    while i < len(array) and array[i] == 0:
                        i += 1

                    if i >= len(array):
                        break

                    j = i+1
                    while j < len(array) and array[j] != 0:
                        j += 1
                    j -= 1

                    if i == j:
                        ans = max(ans, 1)
                    else:
                        length = 1
                        dp = array[i:j+1].copy()
                        for max_length in range(j-i, 0, -1):
                            for k in range(max_length):
                                dp[k] = (length+1) * min(dp[k] // length, dp[k+1] // length)
                                ans = max(ans, dp[k])
                            length += 1
                    i = j+1
                memo[t] = ans
            return memo[t]
                        
        
        
        height = len(matrix)
        width = len(matrix[0])
        
        for i in range(height):
            for j in range(width):
                matrix[i][j] = int(matrix[i][j])
        
        for i in range(height):
            for j in range(width):
                if j > 0 and matrix[i][j] != 0:
                    matrix[i][j] += matrix[i][j-1]
        
        ans = 0
        for j in range(width):
            tmp = [matrix[i][j] for i in range(height)]
            ans = max(ans, max(tmp))
            ans = max(ans, helper(tmp))
        return ans
'''
[["0","0","1","0"],["0","0","1","0"],["0","0","1","0"],["0","0","1","1"],["0","1","1","1"],["0","1","1","1"],["1","1","1","1"]]
[["0","0","1"],["1","1","1"]]
[["1","1","1","0","0"],["1","1","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
[["0"]]
[["1"]]
'''