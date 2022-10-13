class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        ans = (logs[0][1], -logs[0][0])
        preTime = logs[0][1]
        
        for id ,time in logs[1:]:
            t = time - preTime
            ans = max(ans, (t, -id))
            preTime = time
            
        return -ans[1]