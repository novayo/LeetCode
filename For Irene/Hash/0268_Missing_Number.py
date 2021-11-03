class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''
        i = 0
        
        while True:
            if search 1 in nums_set:
                i += 1
            else:
                return i
            
        
        hash
            - set
            - hash table => key: value
        '''
        
        nums_set = set()
        
        # 把所有值加入set => O(n)
        for num in nums:
            nums_set.add(num)
        
        # loop => O(n)
        i = 0
        while True:
            if i in nums_set: # O(1)
                i += 1
            else:
                return i