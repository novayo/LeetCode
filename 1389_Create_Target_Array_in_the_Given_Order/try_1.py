class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        ret = []
        
        for n, i in zip(nums, index):
            ret.insert(i, n)
        return ret
