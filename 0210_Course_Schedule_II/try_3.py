class Node:
    def __init__(self):
        self.parent = 0
        self.children = []

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # build all nodes
        graph = {}
        for i in range(numCourses):
            graph[i] = Node()
        
        # build relationship
        total_edges = 0
        for j, i in prerequisites:
            graph[i].children.append(j)
            graph[j].parent += 1
            total_edges += 1
        
        # find parent=0
        queue = collections.deque()
        for i in range(numCourses):
            if graph[i].parent == 0:
                queue.appendleft(i)
        
        # topological sort
        ans = []
        remove_edges = 0
        while queue:
            node = queue.pop()
            
            ans.append(node)
            
            for child in graph[node].children:
                graph[child].parent -= 1
                remove_edges += 1
                if graph[child].parent == 0:
                    queue.appendleft(child)
        
        return ans if total_edges == remove_edges else []
            
