class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        heap = []
        
        for i, num in enumerate(nums):
            heapq.heappush(heap, (-num, i))
        
        first = heapq.heappop(heap)
        
        if heap:
            second = heapq.heappop(heap)
            if -first[0] >= -second[0]*2:
                return first[1]
            else:
                return -1
        else:
            return 0
