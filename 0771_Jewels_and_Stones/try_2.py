class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        counterS = collections.Counter(S)
        
        ans = 0
        for j in J:
            ans += counterS.get(j, 0)
        return ans