class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        table = collections.defaultdict(list)
        
        for a, b in trust:
            table[a].append(b)
        
        # 找 town judge
        for i in range(1, N+2):
            if i not in table:
                break
        
        if i == N+1:
            return -1
        
        # 看是否到town judge長度為一
        for j in range(1, N+1):
            if j == i:
                continue
            
            if i not in table[j]:
                return -1

        return i
