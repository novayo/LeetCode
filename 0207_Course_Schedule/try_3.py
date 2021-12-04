class Node:
    def __init__(self):
        self.children = []
        self.degree = 0

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # init
        graph = {}
        for i in range(numCourses):
            graph[i] = Node()
        
        # build graph + get total edges
        total_edges = 0
        for i, j in prerequisites:
            graph[j].children.append(i)
            graph[i].degree += 1
            total_edges += 1
        
        # get degree=0
        queue = collections.deque()
        for i in range(numCourses):
            if graph[i].degree == 0:
                queue.appendleft(i)
        
        # bfs
        ans = []
        remove_edges = 0
        while queue:
            node = queue.pop()
            ans.append(node)
            
            for child in graph[node].children:
                graph[child].degree -= 1
                remove_edges += 1
                if graph[child].degree == 0:
                    queue.appendleft(child)
        
        return remove_edges == total_edges
            
