class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        table = collections.defaultdict(int)
        for c in C:
            for d in D:
                table[-(c+d)] += 1
        
        ans = 0
        for b in B:
            for a in A:
                if table.get(a+b):
                    ans += table[a+b]

        return ans
