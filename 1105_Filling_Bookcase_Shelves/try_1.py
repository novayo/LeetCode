class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        '''
        [width, height] & 要照順序排
        
        將題目轉成：求分成k個subarray後，最小高度為何？
        dp[i] = 前i個，分成k層的 的最小高度
        
        
        
        loop i=0~n:
            cur_width = books[i][0]

            loop j=i~0:
                if cur_width + books[j][0] <= shelfWidth:
                    cur_width += books[j][0]
                    cur_height = max(books[i][1], dp[j])
                    dp[i] = min(dp[i], dp[j] + cur_height)
                else:
                    break
        '''
        n = len(books)
        dp = [float('inf')] * (n+1)
        
        dp[0] = 0
        
        for i in range(1, n+1):
            cur_width = 0
            cur_height = 0
            
            # 找從第i層往前，能放就放的最小height
            for j in range(i, -1, -1):
                if cur_width + books[j-1][0] <= shelfWidth:
                    cur_width += books[j-1][0]
                    cur_height = max(cur_height, books[j-1][1])
                    dp[i] = min(dp[i], dp[j-1] + cur_height)
                else:
                    break
        return dp[n]
        
