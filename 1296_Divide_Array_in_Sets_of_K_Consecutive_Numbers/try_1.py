class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k > 0:
            return False
        
        need_delete = set()
        
        
        counter = collections.Counter(nums)
        next_num = list(counter.keys())
        heapq.heapify(next_num)
        
        while next_num:
            start_num = next_num[0]
            while start_num in need_delete:
                heapq.heappop(next_num)
                if next_num:
                    start_num = next_num[0]
                else:
                    break
            if not next_num:
                break
            
            for i in range(k):
                if counter[start_num+i] > 0:
                    counter[start_num+i] -= 1
                    if counter[start_num+i] == 0:
                        need_delete.add(start_num+i)
                else:
                    return False
            
        return True
