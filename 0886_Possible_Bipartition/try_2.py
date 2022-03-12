class UnionFind:
    def __init__(self, n):
        self.parent = {}
        self.rank = {}
        
        for i in range(1, n+1):
            self.parent[i] = i
            self.rank[i] = 0
    
    def same_root(self, node1, node2):
        return self.findParent(node1) == self.findParent(node2)
    
    def findParent(self, node):
        if node != self.parent[node]:
            self.parent[node] = self.findParent(self.parent[node])
        return self.parent[node]
    
    def union(self, node1, node2):
        p1 = self.findParent(node1)
        p2 = self.findParent(node2)
        
        if p1 == p2:
            return
        
        rank1 = self.rank[p1]
        rank2 = self.rank[p2]
        
        if rank1 > rank2:
            self.parent[p2] = p1
        elif rank1 < rank2:
            self.parent[p1] = p2
        else:
            self.parent[p2] = p1
            self.rank[p1] += 1
        
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        graph = collections.defaultdict(list)
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        
        tree = UnionFind(n)
        for a, bs in graph.items():
            for b in bs:
                if tree.same_root(a, b):
                    return False
                tree.union(bs[0], b)
        return True
        
        
        
