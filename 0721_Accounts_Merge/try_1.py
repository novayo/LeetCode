class Union_Find:
    def __init__(self):
        self.root = {}
        self.parent = {}
        
    def add(self, n, root):
        if n not in self.parent:
            self.parent[n] = n
            self.root[n] = root
        
    def findParent(self, n):
        if n != self.parent[n]:
            self.parent[n] = self.findParent(self.parent[n])
        return self.parent[n]
    
    def union(self, n1, n2):
        p1 = self.findParent(n1)
        p2 = self.findParent(n2)
        
        if p1 == p2:
            return
        
        self.parent[p1] = p2
        self.root[p1] = self.root[p2]

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        tree = Union_Find()
        
        for _accounts in accounts:
            root = None
            main_account = None
            for i, account in enumerate(_accounts):
                if i == 0:
                    root = account
                elif i == 1:
                    main_account = account
                    tree.add(main_account, root+'#'+main_account)
                else:
                    tree.add(account, root)
                    tree.union(account, main_account)
        
        merge = collections.defaultdict(set)
        for child, _ in tree.parent.items():
            parent = tree.findParent(child)
            merge[tree.root[parent]].add(child)
        
        ans = []
        for key, value_set in merge.items():
            name = key.split('#')[0]
            ans.append([name] + sorted(list(value_set)))
        return ans