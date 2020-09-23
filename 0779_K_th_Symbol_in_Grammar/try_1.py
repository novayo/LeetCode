class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        '''
        第k的位置，是上一個的第(k+1)//2的位置變得
        如果 k 是奇數，則是上一個的 第一個數字
        如果 k 是偶數，則是上一個的 第二個數字
        '''
        
        # 去往上尋找數字，return 答案
        def recr(n, k):
            
            if n == 1:
                return 0
            
            ret = recr(n-1, (k+1)//2)
            if k % 2 == 0:
                if ret == 0:
                    return 1
                else:
                    return 0
            else:
                if ret == 0:
                    return 0
                else:
                    return 1
        
        return recr(N, K)