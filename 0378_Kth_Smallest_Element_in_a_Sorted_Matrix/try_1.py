class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        return sorted([elem for row in matrix for elem in row])[k-1]
