class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        '''
        subroutine: f(row, col) = f(row-1, col-1) + f(row-1, col)
        base: f(i,j) = 1 where j=0 or j=i
        '''
        dp = {}
        def recr(row, col):
            # dp
            if (row, col) in dp:
                return dp[row, col]
            
            if col == 0 or col == row:
                dp[row, col] = 1
            else:
                dp[row, col] = recr(row-1, col-1) + recr(row-1, col)
            return dp[row, col]
        
        
        
        ret = [1]
        for col in range(1, rowIndex+1):
            ret.append(recr(rowIndex, col))
        
        return ret
