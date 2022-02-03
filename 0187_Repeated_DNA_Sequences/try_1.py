class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        ans = set()
        found = set()
        
        for i in range(n-10+1):
            target = s[i:i+10]
            if target in found:
                ans.add(target)
            found.add(target)
        
        return ans
