class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort
        counter = collections.Counter(nums)
        
        buckets = [[] for _ in range(len(nums)+1)]
        for num, count in counter.items():
            buckets[count].append(num)
        
        ans = []
        for lists in buckets[::-1]:
            ans.extend(lists)
            if len(ans) > k:
                break
        
        return ans[:k]
        
        
