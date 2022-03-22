class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        
        keys = sorted(counter.keys())
        arr = [(key, key*counter[key]) for key in keys]
        
        preKey = -1
        choose = not_choose = 0
        for num, val in arr:
            tmpChoose = choose
            
            if preKey + 1 == num:
                choose = not_choose + val
            else:
                choose = max(tmpChoose + val, not_choose + val)
            
            preKey = num
            not_choose = max(tmpChoose, not_choose)
            
        
        return max(choose, not_choose)