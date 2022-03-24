class Node:
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = Node()
    
    def add(self, nodes):
        root = self.root
        
        for node in nodes:
            if root.children[node].isWord:
                return
            root = root.children[node]
            
        root.isWord = True
        root.children.clear()
    
    def query(self):
        root = self.root
        ans = []
        
        def recr(root, cur_list):
            nonlocal ans
            
            if root.isWord:
                ans.append('/' + '/'.join(cur_list))
                return
            
            for node in root.children.keys():
                recr(root.children[node], cur_list+[node])
        
        recr(root, [])
        return ans

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        tree = Trie()
        
        for path in folder:
            tree.add(path[1:].split('/'))
        
        return tree.query()