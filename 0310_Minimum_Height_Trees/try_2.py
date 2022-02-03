class Node:
    def __init__(self):
        self.parent = 0
        self.children = []

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        all_nodes = n
        
        graph = {}
        for i in range(n):
            graph[i] = Node()
        
        for a, b in edges:
            graph[a].parent += 1
            graph[a].children.append(b)
            graph[b].parent += 1
            graph[b].children.append(a)
        
        
        queue = []
        for i in range(n):
            if graph[i].parent <= 1: 
                queue.append(i)
                
        # 從最外圍一層一層刪除 => topological
        while all_nodes > 2:
            all_nodes -= len(queue)
            
            new_queue = []
            while queue:
                node = queue.pop()
                for child in graph[node].children:
                    graph[child].parent -= 1
                
                    if graph[child].parent == 1:
                        new_queue.append(child)
            queue = new_queue
                    
        return queue
