class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        cache = set()
        ans = set()
        
        for num in nums:
            if num + k in cache:
                ans.add((num, num+k))
            if num - k in cache:
                ans.add((num - k, num))
            
            cache.add(num)
        
        return len(ans)