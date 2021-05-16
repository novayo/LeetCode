class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        '''
        1. 比較兩word最少有幾個不同 => 找出最長的已經有的sub word，答案為len(word1) - 最長長度
           => 不能從尾巴來，因為可能是中間最長，其他兩邊打掉 => 查詢為n^3
        2. 硬爆所有可能
        *3. dp 找出所有可能
        '''
        
        def print_():
            self.print_(dp, word1, word2)
        
        if not word1 and not word2:
            return 0
        elif not word1:
            return len(word2)
        elif not word2:
            return len(word1)
        
        height = len(word1)
        width = len(word2)
        dp = [[0 for _ in range(width)] for _ in range(height)]
        
        # init
        target = word1[0]
        count = 0
        flag = True
        for i in range(width):
            if flag and word2[i] == target: # 因只有一個i，故只能跳過一次i
                flag = False
            else:
                count += 1
            dp[0][i] = count
        
        target = word2[0]
        count = 0
        flag = True
        for i in range(height):
            if flag and word1[i] == target: # 因只有一個i，故只能跳過一次i
                flag = False
            else:
                count += 1
            dp[i][0] = count
        
        # print_()
        
        # loop
        for i in range(1, height):
            for j in range(1, width):
                if word1[i] == word2[j]:
                    dp[i][j] = min(dp[i-1][j-1], dp[i][j-1]+1, dp[i-1][j]+1)
                else:
                    dp[i][j] = min(dp[i-1][j-1]+1, dp[i][j-1]+1, dp[i-1][j]+1)
        
        # print_()
        
        return dp[-1][-1]
        
    
    def print_(self, dp, word1, word2):
        # 第一排
        print(' ', end=' ')
        for word in word2:
            print(word, end=' ')
        print()
        
        # 接下來
        for i in range(len(word1)):
            print(word1[i], end=' ')
            for j in range(len(word2)):
                print(dp[i][j], end=' ')
            print()
        
        print('-----------')