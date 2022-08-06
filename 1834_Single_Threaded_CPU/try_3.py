class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # O(nlogn) time / O(n) space - where n is the length of input array
        tasks = [[v[0], v[1], i] for i, v in enumerate(tasks)]
        tasks.sort()
        
        n = len(tasks)
        cpu_time = i = 0
        min_heap = []
        ans = []
        
        while i < n:
            if len(min_heap) == 0:
                cpu_time = max(cpu_time, tasks[i][0])
            
            while i < n and cpu_time >= tasks[i][0]:
                heapq.heappush(min_heap, (tasks[i][1], tasks[i][2]))
                i += 1
            
            process_time, task_id = heapq.heappop(min_heap)
            cpu_time += process_time
            ans.append(task_id)
        
        while min_heap:
            process_time, task_id = heapq.heappop(min_heap)
            ans.append(task_id)
        
        return ans