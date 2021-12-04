class Node:
    def __init__(self):
        self.children = []
        self.degree = 0
    
class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        # get all source
        sources = set()
        for seq in seqs:
            for s in seq:
                sources.add(s)
                
        # build
        graph = collections.defaultdict(Node)
        for seq in seqs:
            parent = seq[0]
            if parent not in graph:
                graph[parent] = Node()
            for child in seq[1:]:
                graph[parent].children.append(child)
                graph[child].degree += 1
                parent = child
        
        # get degree=0
        queue = collections.deque()
        for key, node in graph.items():
            if node.degree == 0:
                queue.appendleft(key)
        
        # bfs
        index = 0
        result = []
        while queue:
            if len(queue) > 1:
                return False
            node = queue.pop()
            
            if index >= len(org):
                return False
            if node != org[index]:
                return False
            
            
            index += 1
            result.append(node)
            for child in graph[node].children:
                graph[child].degree -= 1
                if graph[child].degree == 0:
                    queue.appendleft(child)
        
        return len(result) == len(sources) and result == org
