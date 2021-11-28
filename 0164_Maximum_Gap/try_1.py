class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        '''
        求數組中，已排序過的數組中，兩數差值最大是多少
        
        我們可以用bucket sort分成0~n-1組（用最大、最小值、長度可計算n）
        之後依照 （數字//n）的商存入bucket中，之後只需要找出每個bucket中的最大值、最小值
        
        而解會在 (bucketN-1的最小值 - bucketN的最大值)取最大
        
        
        bucket sort => 將nums分成n-1組，用商當作key
        bucket_length = ceil((max-min) / n-1) + 1
        
        用dict存有出現的即可，因為python的hash會按照key排序
        '''
        if len(nums) < 2:
            return 0
        
        _min, _max, n = min(nums), max(nums), len(nums)
        
        if _max == _min:
            return 0
        
        buckets = {}
        for num in nums:
            i = (num - _min) * (n-1) // (_max-_min) # 分成0~n-1桶
            
            if i not in buckets:
                buckets[i] = [float('inf'), -float('inf')] # min, max
            buckets[i][0] = min(buckets[i][0], num)
            buckets[i][1] = max(buckets[i][1], num)
        
        ans = 0
        pre_max = None
        for i in range(n):
            if i not in buckets:
                continue
                
            _min, _max = buckets[i]
            
            if pre_max != None:
                ans = max(ans, _min - pre_max)
            else:
                ans = max(ans, _max-_min)
                
            pre_max = _max
        
        return ans
            
