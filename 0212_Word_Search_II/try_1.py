class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.finish = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.finish = True
        
    def search(self, word):
        node = self.root
        for w in word:
            node = node.children.get(w)
            if not node:
                return False
        return node.finish
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(node, i, j, s):
            nonlocal ans
            if node.finish:
                ans.append(s)
                node.finish = False
            if i<0 or j<0 or i>=len(board) or j>=len(board[0]):
                return
            node = node.children.get(board[i][j])
            if not node:
                return
            tmp = board[i][j]
            board[i][j] = "#"
            dfs(node, i-1, j, s+tmp)
            dfs(node, i, j+1, s+tmp)
            dfs(node, i+1, j, s+tmp)
            dfs(node, i, j-1, s+tmp)
            board[i][j] = tmp
            
        ans = collections.deque()
            
        # build trie
        trie = Trie()
        node = trie.root
        for word in words:
            trie.insert(word)
        
        # build queue
        queue = collections.deque()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if node.children.get(board[i][j]):
                    dfs(node, i, j, "")
        return ans
