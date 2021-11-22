class Disjoint_Set:
    def __init__(self):
        self.parent = {}
    
    def add(self, string):
        if string not in self.parent:
            self.parent[string] = string
    
    def isSame(self, s1, s2):
        p1 = self.findParent(s1)
        p2 = self.findParent(s2)
        
        return p1 == p2
    
    def findParent(self, string):
        if string != self.parent[string]:
            self.parent[string] = self.findParent(self.parent[string])
        return self.parent[string]
    
    def union(self, s1, s2):
        p1 = self.findParent(s1)
        p2 = self.findParent(s2)
        
        if p1 == p2:
            return
        else:
            self.parent[p1] = p2
        

class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        '''
        disjoint set to merge two string
        
        if the same means their parents are the same (Same as LC947)
        '''
        if len(sentence1) != len(sentence2):
            return False
        
        # build tree
        tree = Disjoint_Set()
        for s1, s2 in similarPairs:
            tree.add(s1)
            tree.add(s2)
            tree.union(s1, s2)
        
        # find if their parents are the same
        for s1, s2 in zip(sentence1, sentence2):
            # string might not in similarPairs
            tree.add(s1)
            tree.add(s2)
            
            # compare
            if not tree.isSame(s1, s2):
                return False
        return True
        
        
        
        
