class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        def allParents(m, c, who):
            ret = []
            if who == 1:
                for c2 in graph[c]:
                    if c2 == 0:
                        continue
                    ret.append((m, c2, 2))
            else:
                for m2 in graph[m]:
                    ret.append((m2, c, 1))
            return ret
        
        def allChildrenWin(m, c, who):
            if who == 1:
                return all([status[_m][c][2] == 2 for _m in graph[m]])
            else:
                for _c in graph[c]:
                    if _c == 0:
                        continue
                    if status[m][_c][1] != 1:
                        return False
                return True
        
        n = len(graph)
        status = [[[0] * 3 for _ in range(n)] for __ in range(n)]
        
        queue = collections.deque()
        for who in range(1, 3):
            for c in range(1, n):
                status[c][c][who] = 2
                queue.append((c,c,who))
            for c in range(n):
                status[0][c][who] = 1
                queue.append((0,c,who))
        
        while queue:
            m, c, who = queue.popleft()
            s = status[m][c][who]
            
            # 對目前的點來說，如果是mouse贏 且 上一輪是mouse的話 => 上一輪的狀態就是mouse贏
            for m2, c2, who2 in allParents(m, c, who):
                if status[m2][c2][who2] != 0:
                    continue
                    
                if s == who2:
                    status[m2][c2][who2] = s
                    queue.append((m2,c2,who2))
            
                # 對目前的點來說，上一輪是cat的話 且 所有cat的周圍都是老鼠贏 => 上一輪的狀態就是mouse贏
                elif allChildrenWin(m2, c2, who2):
                    status[m2][c2][who2] = 1 if who2 == 2 else 2
                    queue.append((m2,c2,who2))
            
        return status[1][2][1]
