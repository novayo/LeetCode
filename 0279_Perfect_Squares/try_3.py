class Solution:
    def numSquares(self, n: int) -> int:
        '''
        可以先建立平方數表
        dfs+dp，dp={number: 由幾個組成}，dfs=>bottom，回傳有幾個數字
        '''

        if n == 0:
            return 0
        
        square_list = []
        square_set = set()
        for i in range(1, int(sqrt(n))+1):
            square_list.append(i*i)
            square_set.add(i*i)
        square_list.reverse()
        
        dp = {}
        
        def bottom_up(number, square_list, square_set):
            if number in square_set:
                return 1
            
            if number in dp:
                return dp[number]
            
            ret = float('inf')
            for l in square_list:
                if l > number:
                    continue
                    
                ret = min(ret, bottom_up(number-l, square_list, square_set)+1)
            
            dp[number] = ret
            return ret    
            
            
        return bottom_up(n, square_list, square_set)