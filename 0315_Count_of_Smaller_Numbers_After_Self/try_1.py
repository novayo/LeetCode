class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        '''
        n^2 * logn
        '''
        ans = collections.deque()
        s = []
        
        for i in range(len(nums)-1, -1, -1): # n
            num = nums[i]
            index = bisect.bisect_left(s, num) # logn
            s.insert(index, num)    # nlogn
            ans.appendleft(index)
            
        return ans
