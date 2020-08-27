class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted(i*i for i in A)
