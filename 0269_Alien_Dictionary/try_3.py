class Node:
    def __init__(self):
        self.parent = 0
        self.children = set()

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # build graph
        total_edges = 0
        graph = {}
        
        for word in words:
            for w in word:
                if w not in graph:
                    graph[w] = Node()
        
        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]

            length = min(len(word1), len(word2))
            for k in range(length):
                if word1[k] != word2[k]:
                    if word2[k] not in graph[word1[k]].children:
                        graph[word1[k]].children.add(word2[k])
                        graph[word2[k]].parent += 1
                        total_edges += 1
                    break

                # ['abc', 'ab']
                if k+1 == length:
                    if k+1 == len(word2) and k+1 < len(word1):
                        return ""
                
        # find init
        queue = collections.deque()
        for w, node in graph.items():
            if node.parent == 0:
                queue.appendleft(w)
        
        # do topological sort
        ans = ''
        removed_edges = 0
        while queue:
            w = queue.pop()
            
            ans += w
            
            for child in graph[w].children:
                graph[child].parent -= 1
                removed_edges += 1
                
                if graph[child].parent == 0:
                    queue.appendleft(child)
        
        return ans if removed_edges == total_edges else ''

