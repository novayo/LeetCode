class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = collections.defaultdict(list)
        for e, m in enumerate(manager):
            graph[m].append(e)
        
        @functools.lru_cache(None)
        def recr(m):
            if len(graph[m]) == 0:
                return informTime[m]
            return informTime[m] + max(recr(e) for e in graph[m])
        
        return recr(headID)
