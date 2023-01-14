class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        '''
        能加就加 
            => 若總和%3==1 
                => 去除最小的1就好 => 1*餘1 or 2*餘2
            => 若總和%3==2
                => 去除最小的1就好 => 2*餘1 or 1*餘2
        '''
        _sum = 0
        min_remain_1 = [float('inf'), float('inf')]
        min_remain_2 = [float('inf'), float('inf')]
        
        for num in nums:
            _sum += num
            if num % 3 == 1:
                if min_remain_1[0] <= num < min_remain_1[1] :
                    min_remain_1[1] = num
                elif min_remain_1[0] > num:
                    min_remain_1[0], min_remain_1[1] = num, min_remain_1[0]
            elif num % 3 == 2:
                if min_remain_2[0] <= num < min_remain_2[1] :
                    min_remain_2[1] = num
                elif min_remain_2[0] > num:
                    min_remain_2[0], min_remain_2[1] = num, min_remain_2[0]
        
        if _sum % 3 == 1:
            _sum -= min(min_remain_1[0], sum(min_remain_2))
        elif _sum % 3 == 2:
            _sum -= min(sum(min_remain_1), min_remain_2[0])
        
        return _sum

