class Node:
    def __init__(self):
        self.parent = 0
        self.children = []

class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        graph = {}
        for i in range(1, n+1):
            graph[i] = Node()
        
        for a, b in relations:
            graph[a].children.append(b)
            graph[b].parent += 1
        
        
        stack = []
        for i in range(1, n+1):
            if graph[i].parent == 0:
                stack.append(i)
        
        removed_edges = ans = 0
        while stack:
            next_stack = []
            ans += 1
            
            for node in stack:
                for child in graph[node].children:
                    graph[child].parent -= 1
                    removed_edges += 1
                    if graph[child].parent == 0:
                        next_stack.append(child)
            
            stack = next_stack
        
        return ans if removed_edges == len(relations) else -1
