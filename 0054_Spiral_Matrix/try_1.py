class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        
        ans = []
        i = j = 0
        direction = 1 # 0-up, 1-right, 2-down, 3-left
        max_times = len(matrix)*len(matrix[0])
        
        for _ in range(max_times):
            ans.append(matrix[i][j])
            matrix[i][j] = False
            
            if direction % 4 == 0:
                if i-1 == -1 or matrix[i-1][j] == False:
                    direction += 1
                    j += 1
                else:
                    i -= 1
            elif direction % 4 == 1:
                if j+1 == len(matrix[0]) or matrix[i][j+1] == False:
                    direction += 1
                    i += 1
                else:
                    j += 1
            elif direction % 4 == 2:
                if i+1 == len(matrix) or matrix[i+1][j] == False:
                    direction += 1
                    j -= 1
                else:
                    i += 1
            elif direction % 4 == 3:
                if j-1 == -1 or matrix[i][j-1] == False:
                    direction += 1
                    i -= 1
                else:
                    j -= 1
            
        return ans
