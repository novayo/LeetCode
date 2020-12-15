class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        算出個數之後
        找兩次最大值
        '''
        
        counter = collections.Counter(nums)
        
        ans = []
        for key, _ in sorted(counter.items(), key=lambda item: item[1], reverse=True):
            if k == len(ans):
                return ans
            ans.append(key)
        
        
        return ans