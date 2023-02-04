class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        
        diffs = [gas[i] - cost[i] for i in range(n)]
        
        ans = -1
        cnt = 0
        for i, val in enumerate(diffs):
            cnt += val
            if cnt < 0:
                cnt = 0
                ans = -1
            elif ans == -1:
                ans = i
        
        return -1 if sum(diffs) < 0 else ans

