class Node:
    def __init__(self):
        self.children = []
        self.parents = set()
        self.num_of_parents = 0

class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        '''
        先做一次拓樸，把關係找出來，只是要多算一個prerequisites
        
        A->B->C
        B的prerequisites有C
        A的prerequisites有B + C(B的prerequisites)
        
        之後去查詢queries = [a, b]
        b的prerequisites是否有a即可
        '''
        # 建圖
        graph = {}
        for node in range(n):
            graph[node] = Node()
        
        for i, j in prerequisites:
            graph[i].children.append(j)
            graph[j].num_of_parents += 1
        
        # 取出底
        workingQueue = collections.deque()
        for node in graph.keys():
            if graph[node].num_of_parents == 0:
                workingQueue.append(node)
        
        # 執行拓樸
        while workingQueue:
            node = workingQueue.pop()
            
            for child in graph[node].children:
                graph[child].parents.add(node) # 加入此點
                graph[child].parents = graph[child].parents.union(graph[node].parents) # 也加入此點的parents
                graph[child].num_of_parents -= 1
                if graph[child].num_of_parents == 0:
                    workingQueue.append(child)
        
        # 跑query
        ans = []
        for i, j in queries:
            if i in graph[j].parents:
                ans.append(True)
            else:
                ans.append(False)
        
        return ans
