class Node:
    def __init__(self):
        self.children = []
        self.num_of_parents = 0

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 屬於第三種，判斷是否沒有cycle同時找出正確答案
        graph = {}
        for i in range(numCourses):
            graph[i] = Node()
        
        total_edges = 0
        for i, j in prerequisites:
            graph[j].children.append(i)
            graph[i].num_of_parents += 1
            total_edges += 1
        
        workingQueue = collections.deque()
        for node in graph.keys():
            if graph[node].num_of_parents == 0:
                workingQueue.append(node)
        
        ans = []
        remove_edges = 0
        while workingQueue:
            node = workingQueue.pop()
            ans.append(node)
            
            for child in graph[node].children:
                graph[child].num_of_parents -= 1
                remove_edges += 1
                if graph[child].num_of_parents == 0:
                    workingQueue.append(child)
        
        return ans if total_edges == remove_edges else []
