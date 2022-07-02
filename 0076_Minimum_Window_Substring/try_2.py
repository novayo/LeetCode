class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def isValid(counter):
            return all([counter[k] >= v for k, v in standard.items()])
        
        ans = ["", float('inf')]
        standard = collections.Counter(t)
        counter = collections.Counter()
        
        i = 0
        for j in range(len(s)):
            counter[s[j]] += 1
            while i <= j and isValid(counter):
                if j-i+1 < ans[1]:
                    ans = [s[i:j+1], j-i+1]
                counter[s[i]] -= 1
                i += 1
        
        return ans[0]
