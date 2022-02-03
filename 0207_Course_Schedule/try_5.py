class Node:
    def __init__(self):
        self.parent = 0
        self.children = []
        
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        for i in range(numCourses):
            graph[i] = Node()
        
        total_edges = 0
        for a, b in prerequisites:
            total_edges += 1
            graph[a].children.append(b)
            graph[b].parent += 1
        
        queue = collections.deque()
        for i in range(numCourses):
            if graph[i].parent == 0:
                queue.append(i)
        
        removed_edges = 0
        while queue:
            node = queue.pop()
            
            for child in graph[node].children:
                graph[child].parent -= 1
                removed_edges += 1
                
                if graph[child].parent == 0:
                    queue.appendleft(child)
        
        return total_edges == removed_edges
