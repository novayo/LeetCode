class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        ans = 0
        a, b, c, d, Sum = {}, {}, {}, {}, {}
        
        for i in range(len(A)):
            a[A[i]] = a.get(A[i], 0) + 1
            b[B[i]] = b.get(B[i], 0) + 1
            c[C[i]] = c.get(C[i], 0) + 1
            d[D[i]] = d.get(D[i], 0) + 1
        
        for i in a:
            for j in b:
                if i + j in Sum:
                    Sum[i+j] += a[i] * b[j]
                else:
                    Sum[i+j] = a[i] * b[j]
        
        for i in c:
            for j in d:
                if Sum.get(-i-j):
                    ans += Sum[-i-j] * c[i] * d[j]

        return ans
