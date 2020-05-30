class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        ans = []
        i = j = 0
        while i < len(A) and j < len(B):
            if A[i][0] > B[j][1]:
                j += 1
            elif A[i][1] < B[j][0]:
                i += 1
            else:
                start = max(A[i][0], B[j][0])
                end = min(A[i][1], B[j][1])
                if A[i][1] == end:
                    i += 1
                else:
                    j += 1
                ans.append([start, end])
        return ans
