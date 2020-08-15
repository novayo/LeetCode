class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        # binary search
        
        '''
        如果可以在a天等到m束花，
        代表
        可以在a+1天，等到至少m束花
        
        因此可以去測試答案，用binary search
        1. 定義condition
            * 看連續可發芽是否有==k，如果有就可以變成一束花
            * 之後再看看在此a下能做成的花束 >= m的話回傳True
        2. 定義資料範圍
            * min(bloomDay)~max(bloomDay)
            * 只發牙一朵 到 全部發芽
        3. 定義回傳資料
            * 如果不能做成(len < m*k)，則回傳-1
            * 否則回傳天數
        '''
        
        if len(bloomDay) < m * k:
            return -1
        
        def condition(days):
            try_m = 0
            try_k = 0
            
            for bloom in bloomDay:
                if bloom <= days:
                    try_k += 1
                    
                    if try_k == k:
                        try_m += 1
                        try_k = 0
                    
                        if try_m >= m:
                            return True
                else:
                    try_k = 0
            return False
        
        left, right = min(bloomDay), max(bloomDay)
        
        while left < right:
            mid = (left + right) // 2
            
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
