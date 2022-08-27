class Solution:
    def countDigitOne(self, n: int) -> int:
        # O(1) time / O(1) space
        if n < 10:
            return int(n >= 1)
        
        # 算幾位數: O(10)
        tmp_n, k = n, 0
        while tmp_n != 0:
            k, tmp_n = k+1, tmp_n // 10
        
        # init: O(10)
        dp_non1 = [0] * (k+1)
        dp_1 = [0] * (k+1)
        dp_non1[1], dp_1[1] = 0, 1
        
        # get all dp: O(10)
        for _k in range(2, k+1):
            dp_non1[_k] = (dp_non1[_k-1] * 9 + dp_1[_k-1])
            dp_1[_k] = (dp_non1[_k-1] * 9 + dp_1[_k-1]) + pow(10, _k-1)
        
        # recr: O(10)
        def recr(n_string):
            _k = len(n_string)
            if len(n_string) == 0:
                return 0
            elif n_string[0] == '0':
                return recr(n_string[1:])
            elif n_string[0] == '1':
                if len(n_string) == 1:
                    return 1
                # 0, 
                return dp_non1[_k] + (int(n_string[1:]) + 1) + recr(n_string[1:])
            else:
                # 2~9
                return dp_1[_k] + (int(n_string[0]) - 1) * dp_non1[_k] + recr(n_string[1:])
        return recr(str(n))
    
    
