class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        deleted = set()
        i = 1
        while i < len(strs):
            for j, (a, b) in enumerate(zip(strs[i-1], strs[i])):
                if j in deleted:
                    continue
                if a < b:
                    break
                elif a > b:
                    deleted.add(j)
                    i = 0
            i += 1
        
        return len(deleted)
                