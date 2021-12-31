class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        '''
        去記得前3小
        
        [1,2,0,3]
        a = 1
        b = 2
        a = 0    => 可以直接取代，因為b就已經確定至少有一人在b前面
        c = 3    => 3 > b => 代表有三人了
        '''
        a = b = float('inf')
        for num in nums:
            if num <= a:
                a = num
            elif num <= b:
                b = num
            else:
                return True
        
        return False
        
