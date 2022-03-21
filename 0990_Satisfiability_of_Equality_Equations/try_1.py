class UF():
    def __init__(self):
        self.parents = {}
        self.ranks = {}
    
    def add(self, a, b):
        if a not in self.parents:
            self.parents[a] = a
            self.ranks[a] = 0
        if b not in self.parents:
            self.parents[b] = b
            self.ranks[b] = 0
    
    def findParent(self, a):
        if a != self.parents[a]:
            self.parents[a] = self.findParent(self.parents[a])
        return self.parents[a]
    
    def union(self, a, b):
        p1 = self.findParent(a)
        p2 = self.findParent(b)
        
        if p1 == p2:
            return
        
        r1 = self.ranks[p1]
        r2 = self.ranks[p2]
        
        if r1 > r2:
            self.parents[p2] = p1
        elif r1 < r2:
            self.parents[p1] = p2
        else:
            self.parents[p2] = p1
            self.ranks[p1] += 1
        
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        tree = UF()
        
        for string in equations:
            a, eq_string, b = string[0], string[1:3], string[3]
            
            tree.add(a, b)
            if eq_string == '==':
                tree.union(a, b)
        
        for string in equations:
            a, eq_string, b = string[0], string[1:3], string[3]
            
            tree.add(a, b)
            if eq_string == '!=':
                if tree.findParent(a) == tree.findParent(b):
                    return False
        
        return True
               