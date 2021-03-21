class Node:
    def __init__(self):
        self.children = []
        self.num_of_parents = 0

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 判斷有無cycle即可，沒有出現在prerequisites可以隨便修，限制能走完就表示能修完
        graph = {}
        for node in range(numCourses):
            graph[node] = Node()
        
        total_edges = 0
        for i, j in prerequisites:
            graph[i].children.append(j)
            graph[j].num_of_parents += 1
            total_edges += 1

        # 只有底才要去跑（num_of_parents=0）
        workingQueue = collections.deque() 
        for node in graph.keys():
            if graph[node].num_of_parents == 0:
                workingQueue.append(node)
        
        # 跑bfs，並記錄刪除了幾個邊（每跑完一個邊就刪除，最後查看是否有等於總邊即可）
        remove_edges = 0
        while workingQueue:
            node = workingQueue.pop()
            
            for child in graph[node].children:
                graph[child].num_of_parents -= 1
                remove_edges += 1
                if graph[child].num_of_parents == 0:
                    workingQueue.append(child)
        
        return total_edges == remove_edges
