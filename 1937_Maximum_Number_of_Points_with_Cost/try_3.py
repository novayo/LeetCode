class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        '''
        [
        [1,5],
        [2,3],
        [4,2]]
        
           [2,3]
            |      => max(prefix_max[i-1]+ width-1-j, suffix_max[i]+j)
        -> [4,2-1] => right => suffix_max
        -> [4-1,2] => left => prefix_max
        '''
        height, width = len(points), len(points[0])
        
        for i in range(height-2, -1, -1):
            # get right suffix_max
            right = [0] * width
            for j in range(width):
                right[j] = points[i+1][j] - j
            
            suffix_max = [0] * width
            cur_max = -float('inf')
            for j in range(width-1, -1, -1):
                cur_max = max(cur_max, right[j])
                suffix_max[j] = cur_max
            
            # left prefix_max
            left = [0] * width
            for j in range(width):
                left[~j] = points[i+1][~j] - j
            
            prefix_max = [0] * width
            cur_max = -float('inf')
            for j in range(width):
                cur_max = max(cur_max, left[j])
                prefix_max[j] = cur_max
            
            # get answer
            for j in range(width):
                if j == 0:
                    points[i][j] += suffix_max[j]+j
                else:
                    points[i][j] += max(prefix_max[j-1]+ width-1-j, suffix_max[j]+j)
        
        return max(points[0])
