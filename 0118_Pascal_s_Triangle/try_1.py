class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        
        if numRows == 0:
            return []
        ans.append([1])
        
        if numRows == 1:
            return ans
        ans.append([1,1])    
        
        if numRows == 2:
            return ans
        
        for i in range(3, numRows+1):
            tmp = [1]
            for j in range(i-2):
                tmp.append(ans[i-2][j] + ans[i-2][j+1])
            ans.append(tmp + [1])
        return ans
