class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # heap
        counter = collections.Counter(nums)
        
        heap = []
        for num, count in counter.items():
            heapq.heappush(heap, (count, num))
            
            if len(heap) > k:
                heapq.heappop(heap)
        
        ans = []
        for count, num in heap:
            ans.append(num)
        return ans
        
