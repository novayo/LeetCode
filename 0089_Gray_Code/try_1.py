class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0: return [0]
        if n == 1: return [0, 1]
        
        ans = [0, 1]
        count = 1
        while len(ans) < 2**n:
            for a in ans[::-1]:
                ans.append(a + 2**count)
            count += 1
        return ans
