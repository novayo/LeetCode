class UF:
    def __init__(self):
        self.group_info = collections.defaultdict(int) # length: count
        self.root_length = collections.defaultdict(int) # node: size
        self.parent = {}
    
    def add(self, i):
        if i not in self.parent:
            self.parent[i] = i
            self.root_length[i] = 1
            self.group_info[1] += 1
    
    def findParent(self, i):
        if i != self.parent[i]:
            self.parent[i] = self.findParent(self.parent[i])
        return self.parent[i]
    
    def union(self, i1, i2):
        if i1 not in self.parent or i2 not in self.parent:
            return
        
        p1 = self.findParent(i1)
        p2 = self.findParent(i2)
        
        if p1 == p2:
            return
        
        # get length
        r1 = self.root_length[p1]
        r2 = self.root_length[p2]
        
        self.group_info[r1] -= 1
        self.group_info[r2] -= 1
        
        # merge length
        if self.group_info[r1] == 0:
            del self.group_info[r1]
        if self.group_info[r2] == 0:
            del self.group_info[r2]
            
        self.group_info[r1+r2] += 1
        
        # union
        if r1 > r2:
            self.root_length[p1] = r1+r2
            self.parent[p2] = p1
        elif r1 < r2:
            self.root_length[p2] = r1+r2
            self.parent[p1] = p2
        else:
            self.root_length[p2] = r1+r2
            self.parent[p1] = p2

class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        tree = UF()
        ans = -1
        
        for i, a in enumerate(arr):
            tree.add(a)
            tree.union(a-1, a)
            tree.union(a, a+1)
            
            if m in tree.group_info:
                ans = i+1
        
        return ans
            