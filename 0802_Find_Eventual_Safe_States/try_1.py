class Node:
    def __init__(self):
        self.children = 0
        self.parent = []

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        
        # build
        table = {}
        for node in range(n):
            table[node] = Node()
        
        for node, children in enumerate(graph):
            table[node].children = len(children)
            for child in children:
                table[child].parent.append(node)
        
        # init
        queue = collections.deque()
        for node in range(n):
            if table[node].children == 0:
                queue.appendleft(node)
        
        # loop
        ans = []
        while queue:
            node = queue.pop()
            
            ans.append(node)
            
            for p in table[node].parent:
                table[p].children -= 1
                if table[p].children == 0:
                    queue.appendleft(p)
        
        return sorted(ans)