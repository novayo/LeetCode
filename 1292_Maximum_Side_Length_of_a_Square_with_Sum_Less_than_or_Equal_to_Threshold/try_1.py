
class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        '''
        mat = 
       0[0,0,0,0,0,0,0
       0[1,1,3,2,4,3,2],
       0[1,1,3,2,4,3,2],
       0[1,1,3,2,4,3,2]], 
        1~300
        10**4
        threshold = 100
        
        mat = [[]]
        return 0 if none
        
        => presum
        => function => 從(i,j,length) => 的面積
        => 大到小 
            => max length of square => every point
        '''
        height = len(mat)
        width = len(mat[0])
        presum = [[0] * (width+1) for _ in range(height+1)]
        
        # calculate presum
        for i in range(1, height+1):
            for j in range(1, width+1):
                presum[i][j] = presum[i-1][j] + presum[i][j-1] - presum[i-1][j-1] + mat[i-1][j-1]
        
        
        def getArea(i, j, length):
            new_i, new_j = i+length-1, j+length-1
            
            if new_i >= height+1 or new_j >= width+1:
                return -1
            
            return presum[new_i][new_j] - presum[i-1][new_j] - presum[new_i][j-1] + presum[i-1][j-1]
        
        def condition(length):
            for i in range(1, height+1):
                for j in range(1, width+1):
                    area = getArea(i, j, length)
                    
                    if area == -1:
                        break
                    
                    if area <= threshold:
                        return True
            return False
        
        max_length = max(height, width)
        ans = 0
        l, r = 1, max_length
        while l <= r:
            mid = l + (r-l) // 2
            if condition(mid):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
                    
        return ans
