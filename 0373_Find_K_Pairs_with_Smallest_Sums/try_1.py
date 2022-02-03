class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        n = len(nums1)
        m = len(nums2)
        max_heap = []
        
        for n1 in nums1:
            
            if len(max_heap) >= k and n1 + nums2[0] >= -max_heap[0][0]:
                break
            
            for n2 in nums2:
                sum = n1 + n2
                
                if len(max_heap) < k:
                    heapq.heappush(max_heap, (-sum, (n1, n2)))
                elif sum < -max_heap[0][0]:
                    heapq.heappush(max_heap, (-sum, (n1, n2)))
                    heapq.heappop(max_heap)
                else:
                    break
        
        ans = []
        for sum, tuples in max_heap:
            ans.append(tuples)
        return ans
                    
                
