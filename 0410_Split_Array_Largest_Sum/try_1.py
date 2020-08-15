class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        # binary search
        
        '''
        如果答案是a，那就一定可以切割成m等分
        也就代表說
        答案大於a的話，就可以切割成小於m等分
        
        因此就可以用binary search
        1. 定義condition
            * 如果a能使答案小於m，則回傳true
        2. 定義資料範圍
            * 資料範圍一定是 max(nums) ~ sum(nums)
        3. 定義回傳值
            * 再看看
        '''
        
        def condition(try_ans):
            try_sum = 0
            try_m = 1
            
            for num in nums:
                try_sum += num
                if try_sum > try_ans:
                    try_m += 1
                    try_sum = num
                    
                    if try_m > m:
                        return False
            
            return True
        
        left, right = max(nums), sum(nums)
        
        while left < right:
            mid = (left + right) // 2
            
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
