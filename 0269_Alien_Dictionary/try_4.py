class Node:
    def __init__(self):
        self.children = set()
        self.parents = 0
    
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        '''
        t -> f
        w -> e
        r -> t
        e -> r
        '''
        n = len(words)
        total_edges = 0
        graph = {}
        for word in words:
            for w in word:
                if w not in graph:
                    graph[w] = Node()
        
        for i in range(n-1):
            word1 = words[i]
            word2 = words[i+1]
            
            length = min(len(word1), len(word2))
            for _i in range(length):
                if word1[_i] != word2[_i]:
                    if word2[_i] not in graph[word1[_i]].children:
                        graph[word1[_i]].children.add(word2[_i])
                        graph[word2[_i]].parents += 1
                        total_edges += 1
                    break
                    
                if _i+1 == length and len(word1) > len(word2):
                    return ''
        
        que = collections.deque()
        for w, node in graph.items():
            if node.parents == 0:
                que.append(w)
        
        
        ans = ''
        remove_edges = 0
        while que:
            w = que.popleft()
            node = graph[w]
            
            ans += w
            
            for child in node.children:
                remove_edges += 1
                graph[child].parents -= 1
                if graph[child].parents == 0:
                    que.append(child)
        
        return ans if total_edges == remove_edges else ""
