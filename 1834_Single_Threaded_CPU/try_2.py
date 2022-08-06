class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        tasks = sorted([[e, p, i] for i, (e, p) in enumerate(tasks)])
        
        ans = []
        pq = []
        cur_time = i = 0
        
        while i < n:
            if len(pq) == 0 and cur_time < tasks[i][0]:
                cur_time = tasks[i][0]
            
            while i < n and tasks[i][0] <= cur_time:
                heapq.heappush(pq, (tasks[i][1], tasks[i][2]))
                i += 1
            
            p, taskid = heapq.heappop(pq)
            cur_time += p
            ans.append(taskid)
        
        while pq:
            _, taskid = heapq.heappop(pq)
            ans.append(taskid)
        
        return ans
