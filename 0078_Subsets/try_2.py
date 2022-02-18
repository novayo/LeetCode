class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        dfs bottom-up
        '''
        n = len(nums)
        
        def dfs(index):
            if index >= n:
                return [[]]
            
            forehead = dfs(index+1)
            ret = forehead.copy()
            for _list in forehead:
                ret.append([nums[index]] + _list)
            return ret
        
        return dfs(0)
            