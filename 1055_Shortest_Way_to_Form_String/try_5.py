class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        # O(mn) time / O(1) space
        
        source_set = set(source)
        for t in target:
            if t not in source_set:
                return -1
        
        m, n = len(source), len(target)
        
        j = ans = 0
        while j < n:
            i = 0
            while i < m and j < n:
                if source[i] == target[j]:
                    j += 1
                i += 1
            ans += 1
        
        return ans if ans > 0 else -1
