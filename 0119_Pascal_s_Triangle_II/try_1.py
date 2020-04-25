class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1]
        a = b = 1
        for i in range(1, rowIndex+1):
            a *= i
            b *= rowIndex-i+1
            ans.append(b // a)
        return ans
