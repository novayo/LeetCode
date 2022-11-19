class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        def gcd(a, b):
            if a > b:
                a, b = b, a
                
            if b % a == 0:
                return a
            return gcd(b%a, a)
        
        
        ans = 0
        for i in range(len(nums)):
            old_lcm = nums[i]
            if old_lcm == k:
                ans += 1
            
            for j in range(i+1, len(nums)):
                lcm = (old_lcm * nums[j]) // gcd(old_lcm, nums[j])
                if lcm == k:
                    ans += 1
                elif lcm > k:
                    break
                old_lcm = lcm
        return ans
