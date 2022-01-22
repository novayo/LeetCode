class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks_list = []
        for i, (e_time, q_time) in enumerate(tasks):
            tasks_list.append((e_time, q_time, i))
        tasks_list.sort()
        
        available = []
        cur_time = 0
        ans = []
        i = 0
        while len(ans) < len(tasks):
            while i < len(tasks_list) and (tasks_list[i][0] <= cur_time or not available):
                heapq.heappush(available, (tasks_list[i][1], tasks_list[i][2]))
                cur_time = max(cur_time, tasks_list[i][0])
                i += 1
            
            q_time, index = heapq.heappop(available)
            cur_time += q_time
            ans.append(index)

        return ans
