class Node:
    def __init__(self):
        self.parent = 0
        self.children = []

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # build
        total_edges = 0
        graph = {}
        for course in range(numCourses):
            graph[course] = Node()
        
        
        for i, j in prerequisites:
            graph[i].parent += 1
            graph[j].children.append(i)
            total_edges += 1
        
        # find init pos
        queue = collections.deque()
        for course in range(numCourses):
            if graph[course].parent == 0:
                queue.appendleft(course)
        
        # do topological sort
        sort_list = []
        removed_edges = 0
        while queue:
            course = queue.pop()
            
            sort_list.append(course)
            
            for child in graph[course].children:
                graph[child].parent -= 1
                removed_edges += 1
                
                if graph[child].parent == 0:
                    queue.appendleft(child)
        
        return sort_list if total_edges == removed_edges else []
