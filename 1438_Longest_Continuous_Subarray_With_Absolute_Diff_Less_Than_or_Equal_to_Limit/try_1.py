class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        '''
        priority_queue
            * min => [value, index]
            * max => [-value, index]
        
        need_to_delete = set()
        
        while j < len(nums):
            ans = max(ans, j-i)
            
            if j-i > limit:
                need_to_delete.add(i)
                i += 1
            
            while not valid that item abs(diff) between max and min:
                if i != min and i != max:
                    need_to_delete.add(i)
                elif i == min:
                    while minHeap and minHeap[0]'s index in need_to_delete:
                        minHeap.pop()
                elif i == max:
                    while maxHeap and maxHeap[0]'s index in need_to_delete:
                        maxHeap.pop()
                i += 1
            j += 1
        '''
        minHeap = []
        maxHeap = []
        need_to_delete = set()
        length = len(nums)
        ans = i = j = 0
        while j < length:
            n = nums[j]
            heapq.heappush(minHeap, (n, j))
            heapq.heappush(maxHeap, (-n, j))
            
            while i <= j and abs(n-minHeap[0][0]) > limit or abs(n+maxHeap[0][0]) > limit:
                need_to_delete.add(i)
                i += 1
            
                # maintain heap
                while minHeap and minHeap[0][1] in need_to_delete:
                    heapq.heappop(minHeap)

                while maxHeap and maxHeap[0][1] in need_to_delete:
                    heapq.heappop(maxHeap)
            
            ans = max(ans, j-i+1)
            j += 1
        
        return ans
        
