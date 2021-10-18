class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [[1]]
        
        for layer in range(2, numRows+1):
            cur = [1]
            
            for index in range(1, layer-1):
                cur.append(dp[-1][index-1] + dp[-1][index])
            
            cur.append(1)
            dp.append(copy.deepcopy(cur))
        
        return dp