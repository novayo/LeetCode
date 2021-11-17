class Union_Find:
    def __init__(self):
        self.parent = {}
        self.roots = 0
    
    def add(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.roots += 1
    
    def findParent(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.findParent(self.parent[x])
        return self.parent[x]
    
    def union(self, x1, x2):
        p1 = self.findParent(x1)
        p2 = self.findParent(x2)
        
        if p1 != p2:
            self.parent[p1] = p2
            self.roots -= 1

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        '''
        因為只要是有same raw or same col => 就可以收成一點
        可以先整理 raw => 有哪些點, col => 有哪些點
        
        1. 每次bfs時要找出同raw, col的
        2. 整理成同一個row, col
            => 把pos的x, y綁在一起
        '''
        tree = Union_Find()
        for stone in stones:
            x = str(stone[0]) + 'x'
            y = str(stone[1]) + 'y'
            
            tree.add(x)
            tree.add(y)
            
            tree.union(x, y)
        
        return len(stones) - tree.roots
