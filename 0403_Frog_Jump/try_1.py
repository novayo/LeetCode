class Solution:
    def canCross(self, stones: List[int]) -> bool:
        indices = {}
        for i, s in enumerate(stones):
            indices[s] = i
        
        memo = set()
        def dfs(idx, step):
            if idx == len(stones)-1:
                return True
            if step == 0:
                return False
            
            if (idx, step) not in memo:
                for s in [step-1, step, step+1]:
                    next_pos = stones[idx] + s
                    if next_pos in indices:
                        if dfs(indices[next_pos], s):
                            return True
                memo.add((idx, step))
            return False
        
        if 1 in indices:
            return dfs(1, 1)
        else:
            return False