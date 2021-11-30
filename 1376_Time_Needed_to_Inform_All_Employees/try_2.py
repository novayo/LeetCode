class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        '''
        manager 的 總時間 = manager本身的時間 + 下屬的最大值
        '''
        
        graph = collections.defaultdict(list)
        for i in range(len(manager)):
            graph[manager[i]].append(i)
        
        def dfs(ID):
            ans = 0
            for employee in graph.get(ID, []):
                ans = max(ans, dfs(employee) + informTime[ID])
            return ans
        
        return dfs(headID)
