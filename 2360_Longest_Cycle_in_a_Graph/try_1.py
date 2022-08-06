class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        # O(n) time / O(n) space
        ans = -1
        n = len(edges)
        status = [-1] * n
        
        for i in range(n):
            if status[i] != -1:
                continue
            
            status[i] = 0
            candidates = set([i])
            level = 1
            i = edges[i]
            while i != -1:
                if status[i] == -1:
                    status[i] = level
                elif status[i] != -1 and i in candidates:
                    ans = max(ans, level - status[i])
                    break
                else:
                    break
                    
                candidates.add(i)
                level += 1
                i = edges[i]
        return ans