class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        
        def helper(a, b):
            # a ^ x = b
            x = ""
            for d1, d2 in zip(bin(a)[2:].zfill(32), bin(b)[2:].zfill(32)):
                if d2 == "1":
                    x += "1" if d1 == "0" else "0"
                else:
                    x += d1
            return int(x, 2)
            
        n = len(pref)
        
        ans = [pref[0]]
        for i in range(1, n):
            ans.append(helper(pref[i - 1], pref[i]))

        return ans