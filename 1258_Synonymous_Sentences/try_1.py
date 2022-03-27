class UF:
    def __init__(self):
        self.parents = {}
        self.ranks = {}
    
    def add(self, n):
        if n not in self.parents:
            self.parents[n] = n
            self.ranks[n] = 0
    
    def findParent(self, n):
        if n != self.parents[n]:
            self.parents[n] = self.findParent(self.parents[n])
        return self.parents[n]
    
    def union(self, n1, n2):
        self.add(n1)
        self.add(n2)
        p1 = self.findParent(n1)
        p2 = self.findParent(n2)
        
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
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        # build tree
        tree = UF()
        for a, b in synonyms:
            tree.union(a, b)
        
        # get group => key=root, value=set()
        group = collections.defaultdict(set)
        for a, b in synonyms:
            pa = tree.findParent(a)
            pb = tree.findParent(b)
            
            group[pa].add(a)
            group[pb].add(b)
        
        # sort group
        for key in group.keys():
            group[key] = sorted(list(group[key]))
        
        # get answer
        text = text.split(' ')
        def recr(i):
            if i >= len(text):
                return ['']
            
            ret = []
            if text[i] not in tree.parents:
                for t in recr(i+1):
                    ret.append(text[i] + ' ' + t)
            else:
                for text_i in group[tree.findParent(text[i])]:
                    for t in recr(i+1):
                        ret.append(text_i + ' ' + t)
            return ret
        
        ans = recr(0)
        for i in range(len(ans)):
            ans[i] = ans[i][:-1]
        return ans