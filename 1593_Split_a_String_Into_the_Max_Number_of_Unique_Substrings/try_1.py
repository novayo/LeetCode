class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        # time => O(n!)
        # space => O(2n)
        def dfs(i, chose_set):
            if i >= len(s):
                return 0
            
            ret = -float('inf')
            for j in range(i, len(s)):
                target = s[i:j+1]
                if target in chose_set:
                    continue
                
                chose_set.add(target)
                ret = max(ret, dfs(j+1, chose_set))
                chose_set.remove(target)
            return ret + 1
        
        return dfs(0, set())
