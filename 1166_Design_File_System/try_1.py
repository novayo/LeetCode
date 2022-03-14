class Node:
    def __init__(self, val=-1):
        self.val = val
        self.children = collections.defaultdict(Node)

class FileSystem:

    def __init__(self):
        self.trie = Node()

    def createPath(self, path: str, value: int) -> bool:
        if not self.isValid(path):
            return False
        
        split_path = path[1:].split('/')
        
        # search
        root = self.trie
        for _path in split_path[:-1]:
            if _path not in root.children:
                return False
            root = root.children[_path]
        
        # check the last element
        if split_path[-1] in root.children:
            return False
        else:
            root.children[split_path[-1]] = Node(value)
            return True

    def get(self, path: str) -> int:
        if not self.isValid(path):
            return -1
        
        split_path = path[1:].split('/')
        
        # search
        root = self.trie
        for _path in split_path[:-1]:
            if _path not in root.children:
                return -1
            root = root.children[_path]
        
        # check the last element
        if split_path[-1] in root.children:
            return root.children[split_path[-1]].val
        else:
            return -1
        
    def isValid(self, path):
        return not (not path or path == '/')


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)