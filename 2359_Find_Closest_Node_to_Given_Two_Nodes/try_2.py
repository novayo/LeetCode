class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def bfs(node):
            arr = [float('inf')] * L
            que = collections.deque()
            
            arr[node] = steps = 0
            que.appendleft(node)
            while que:
                _node = que.pop()
                visit = edges[_node]
                
                if visit == -1 or arr[visit] <= steps:
                    continue
                
                steps += 1
                arr[visit] = steps
                que.appendleft(visit)
                
            return arr
            
        
        L = len(edges)
        dp1 = bfs(node1)
        dp2 = bfs(node2)
        
        ans = min_steps = float('inf')
        for i, (v1, v2) in enumerate(zip(dp1, dp2)):
            tmp = max(v1, v2)
            if tmp < min_steps:
                min_steps = tmp
                ans = i
        
        return ans if ans < float('inf') else -1
