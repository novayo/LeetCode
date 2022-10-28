class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        def gcd(a, b):
            if a > b:
                a, b = b, a
            if b % a == 0:
                return a
            return gcd(b % a, a)
        
        n = len(nums)
        
        ans = 0
        for i in range(n):
            g = nums[i]
            if g == k:
                ans += 1
            for j in range(i + 1, n):
                g = gcd(g, nums[j])
                if g == k:
                    ans += 1
                
                if g % k != 0:
                    break
                    
        return ans