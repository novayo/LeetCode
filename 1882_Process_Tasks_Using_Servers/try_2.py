class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        '''
        free server
        busy server
        
        enque task
        
        if free server:
            handle one task => busy server
            cur_time += 1
        else:
            cur_time = busy server[0]
            
        handle busy server
        
        '''
        n = len(tasks)
        free_server = [] # (weight, idx)
        busy_server = [] # (finish time, weight, idx)
        
        for i, weight in enumerate(servers):
            heapq.heappush(free_server, (weight, i))
        
        ans = []
        idx_task = 0
        cur_time = 0
        while idx_task < n:
            if free_server and idx_task < n:
                weight, server = heapq.heappop(free_server)
                heapq.heappush(busy_server, (cur_time + tasks[idx_task], weight, server))
                ans.append(server)
                idx_task += 1
                cur_time = max(cur_time, idx_task)
            else:
                cur_time = busy_server[0][0]
            
            while busy_server and busy_server[0][0] <= cur_time:
                _, weight, server = heapq.heappop(busy_server)
                heapq.heappush(free_server, (weight, server))
        return ans
            
            
            
            
