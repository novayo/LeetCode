class Node:
    def __init__(self, v):
        self.val = v
        self.children = []

class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        graph = {}
        for p, c in zip(ppid, pid):
            if p not in graph:
                graph[p] = Node(p)
            graph[p].children.append(c)
        
        def dfs(node):
            if not node:
                return []
            if node not in graph:
                return [node]
            
            ret = [node]
            for c in graph[node].children:
                ret += dfs(c)
            return ret
        
        return dfs(kill)
