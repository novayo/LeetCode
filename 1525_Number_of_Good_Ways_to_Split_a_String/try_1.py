class Solution:
    def numSplits(self, s: str) -> int:
        left = collections.defaultdict(int)
        right = collections.defaultdict(int)
        
        for i in range(len(s)):
            if i == 0:
                left[s[i]] += 1
            else:
                right[s[i]] += 1
        
        ans = 0
        for i in range(1, len(s)):
            if len(left) > len(right):
                break
            
            if len(left) == len(right):
                ans += 1
            
            left[s[i]] += 1
            right[s[i]] -= 1
            
            if right[s[i]] == 0:
                del right[s[i]]
            
        return ans
