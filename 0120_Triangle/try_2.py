class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        '''
        把左右兩邊加起來之後，就會轉成帕斯卡三角形了
        '''
        
        for i in range(1, len(triangle)):
            triangle[i][0] += triangle[i-1][0]
            triangle[i][-1] += triangle[i-1][-1]
        
        for i in range(1, len(triangle)-1):
            for j in range(len(triangle[i])-1):
                triangle[i+1][j+1] += min(triangle[i][j], triangle[i][j+1])
        
        return min(triangle[-1])
