class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        ans = 1
        cache = set()
        remainder = 1 # long long int
        
        while remainder > 0:
            # 補齊
            while remainder < k:
                ans += 1
                remainder *= 10
                remainder += 1
                
            remainder %= k
            if remainder in cache:
                return -1
            cache.add(remainder)
        
        return ans