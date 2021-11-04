class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        
        heap = []
        for key, value in counter.items():
            
            if len(heap) < k:
                heapq.heappush(heap, (value, key))
            elif heap[0][0] < value:
                heapq.heappop(heap)
                heapq.heappush(heap, (value, key))
        
        ans = [0] * len(heap)
        for i in range(len(heap)):
            ans[i] = heap[i][1]
        return ans
