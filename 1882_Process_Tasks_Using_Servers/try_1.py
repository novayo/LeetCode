class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        free_servers = [] # server, index
        busy_servers = [] # finish time, server, index
        ans = []
        
        # init
        current_time = 0
        for i, server in enumerate(servers):
            heapq.heappush(free_servers, (server, i))
        
        # loop
        for i, task in enumerate(tasks): 
            if not free_servers:
                current_time = busy_servers[0][0]
            else:
                current_time = max(current_time, i)
            
            # adjust busy_servers
            while busy_servers and busy_servers[0][0] <= current_time:
                _, server, index = heapq.heappop(busy_servers)
                heapq.heappush(free_servers, (server, index))
            
            server, index = heapq.heappop(free_servers)
            heapq.heappush(busy_servers, (current_time + task, server, index))
            ans.append(index)
            
        return ans