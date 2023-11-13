class Solution:
    def countSubstrings(self, s: str) -> int:
        def expandFromCenter(i, j):
            count = 0
            while i >= 0 and j < length:
                if s[i] != s[j]:
                    break
                i, j = i-1, j+1
                count += 1
            return count
        
        ans = 0
        length = len(s)
        for i in range(length):
            ans += expandFromCenter(i, i)

            if i + 1 < length and s[i] == s[i+1]:
                ans += expandFromCenter(i, i+1)
        return ans
