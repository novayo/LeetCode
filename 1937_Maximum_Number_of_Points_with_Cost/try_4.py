class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        '''
        [4,.....|....,2]
        pre_minus first => dp1[j] = val-j
        find max from 0~j-1 => dp2[j] cur_max => val - j
        find max from end~j => dp3[j] cur_max => val + j
        '''
        height, width = len(points), len(points[0])
        
        for i in range(height-2, -1, -1):
            dp1 = []
            for j in range(width-1, -1, -1):
                dp1.append(points[i+1][j] - (width-1-j))
            dp1.reverse()
                
            left_max = []
            cur_max = -float('inf')
            for j in range(width):
                cur_max = max(cur_max, dp1[j])
                left_max.append(cur_max)
            
            dp1 = []
            for j in range(width):
                dp1.append(points[i+1][j] - j)
            
            right_max = []
            cur_max = -float('inf')
            for j in range(width-1, -1, -1):
                cur_max = max(cur_max, dp1[j])
                right_max.append(cur_max)
            right_max.reverse()
            
            for j in range(width):
                left = (left_max[j-1] + (width-1-j)) if j > 0 else 0
                right = (right_max[j]) + j
                points[i][j] += max(left, right)
        
        return max(points[0])
