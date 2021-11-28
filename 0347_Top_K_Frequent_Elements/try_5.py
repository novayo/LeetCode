class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        bucket sort => freq as bucket => get num by freq
        '''
        
        buckets = [[] for _ in range(len(nums)+1)]
        counter = collections.Counter(nums)
        
        for num, freq in counter.items():
            buckets[freq].append(num)
        
        ans = []
        for num_list in buckets[::-1]:
            ans.extend(num_list)
            if len(ans) > k:
                break
        
        return ans[:k]
