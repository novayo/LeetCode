class Node:
    def __init__(self):
        self.parent = 0
        self.children = []

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Topological sort
        graph = {}
        all_edges = 0
        
        # build tree
        for course in range(numCourses):
            graph[course] = Node()
        
        for i, j in prerequisites:
            graph[j].parent += 1
            graph[i].children.append(j)
            all_edges += 1
        
        # get init points
        queue = collections.deque()
        for course in range(numCourses):
            if graph[course].parent == 0:
                queue.appendleft(course)
        
        # do topological sort
        remove_edge = 0
        while queue:
            course = queue.pop()
            
            for child in graph[course].children:
                graph[child].parent -= 1
                remove_edge += 1
                
                if graph[child].parent == 0:
                    queue.appendleft(child)
        
        return all_edges == remove_edge
            
            
