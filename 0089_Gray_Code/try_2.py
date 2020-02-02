class Solution:
    def grayCode(self, n: int) -> List[int]:
        result = collections.deque()
        
        val = 2 ** n
        for i in range(val):
            result.append(i ^ (i>>1))
        return result
