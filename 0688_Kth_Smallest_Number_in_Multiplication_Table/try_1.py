class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        # binary search
        '''
        這裡可以看成這樣
        
        我去猜4在這個裡面是站在第幾個位置，
        而4要怎麼看他是站在第幾格呢？
        就去看，第一行 他站了幾格，第二航站了幾格，但三行站了幾格
        而要去看每一行站了幾格，就直接將4//1 4//2 4//3，
        4//1 = 4 => 第一行，但這個大於n，因此就取3 (n=3)，代表站了1 2 3
        4//2 = 2 => 第二行，站了2格，2 4
        4//3 = 1 => 第三行，站了1格，3
        
        因此condition就出來了
        而範圍是1~m*n
        
        而，
        如果4//5 == 0之後就不用再繼續跑了，可以中斷迴圈
        而大於k的時候也可以直接回傳true
        '''
        
        def condition(number):
            count = 0
            for i in range(1, m+1):
                tmp = number // i
                if tmp == 0:
                    break
                count += min(tmp, n)
                if count >= k:
                    return True
            return count >= k
        
        left, right = 1, m*n
        while left < right:
            mid = left + (right - left) // 2
            if condition(mid):
                right = mid
            else:
                left = mid+1
        return left
