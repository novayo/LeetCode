class Solution:
    def grayCode(self, n: int) -> List[int]:
        ans = []
        val = 1 << n
        for i in range(val):
            ans.append(i ^ i >> 1)
        return ans
