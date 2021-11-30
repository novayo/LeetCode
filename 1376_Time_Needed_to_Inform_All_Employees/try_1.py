class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        '''
        先建立manager tree => manager[i] 下面有i
        
        做bfs
        time 去紀錄總時間
        
        用dict當作queue => manager: remain time
            每次從remain time取最小，把所有人都-最小值
            把0的從dict刪除，並把旗下的加入dict
        '''
        
        graph = collections.defaultdict(list)
        for i in range(len(manager)):
            employee = i
            manager_ = manager[i]
            
            graph[manager_].append(employee)
        
        queue = {headID: informTime[headID]}
        ans = 0
        
        while queue:
            
            # 取最小remain time
            min_time = min(queue.values())
            
            # 把0的從dict刪除，並把旗下的加入dict
            deleted_key = set()
            for key in queue.keys():
                queue[key] -= min_time
                if queue[key] == 0:
                    deleted_key.add(key)
            
            for key in deleted_key:
                del queue[key]
                for employee in graph.get(key, []):
                    queue[employee] = informTime[employee]
            
            ans += min_time
        
        return ans
