class Node:
    def __init__(self):
        self.parents = 0
        self.children = set()

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        ans = ''
        total_edges = removed_edges = 0
        
        # init graph
        graph = {}
        for word in words:
            for w in word:
                graph[w] = Node()

        # build graph
        for i in range(1, len(words)):
            word1, word2 = words[i-1], words[i]

            if len(word1) > len(word2) and word1[:len(word2)] == word2:
                return ''

            for j in range(min(len(word1), len(word2))):
                w1, w2 = word1[j], word2[j]
                if w1 != w2:
                    if w2 not in graph[w1].children:
                        graph[w1].children.add(w2)
                        graph[w2].parents += 1
                        total_edges += 1
                    break
                    
        # init queue
        queue = collections.deque()
        for w in graph.keys():
            if graph[w].parents == 0:
                queue.appendleft(w)
        
        # loop queue
        while queue:
            w = queue.pop()
            ans += w

            for child in graph[w].children:
                removed_edges += 1
                graph[child].parents -= 1
                if graph[child].parents == 0:
                    queue.appendleft(child)
        
        return ans if total_edges == removed_edges else ''

