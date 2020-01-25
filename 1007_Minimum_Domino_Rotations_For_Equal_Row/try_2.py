class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        n = len(A)
        validNumbers = (A[0], B[0])
        for x in validNumbers:
            countA = 0
            countB = 0
            for i in range(n):
                countA += (x == A[i])
                countB += (x == B[i])
                if x != B[i] and x != A[i]:
                    break            
            if i == n-1:
                return n - max(countA,countB)
        return -1

