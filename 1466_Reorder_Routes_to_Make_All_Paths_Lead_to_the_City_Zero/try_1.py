class Node:
    def __init__(self):
        self.parent = []
        self.children = []

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = {}
        for a, b in connections:
            if a not in graph:
                graph[a] = Node()
            if b not in graph:
                graph[b] = Node()
            
            graph[a].children.append(b)
            graph[b].parent.append(a)
        
        ans = 0
        cache = set([0])
        queue = collections.deque([0])
        while queue:
            node = queue.pop()
            
            for p in graph[node].parent:
                if p not in cache:
                    cache.add(p)
                    queue.appendleft(p)
            
            for c in graph[node].children:
                if c not in cache:
                    cache.add(c)
                    queue.appendleft(c)
                    ans += 1
        return ans
