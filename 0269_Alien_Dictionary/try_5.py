class Solution:
    def alienOrder(self, words: List[str]) -> str:
        '''
        t -> f
        w -> e
        r -> t
        e -> r
        '''
        remove_edges = total_edges = 0
        n = len(words)
        graph = {}
        for word in words:
            for w in word:
                graph[w] = {
                    'parents': 0,
                    'children': set()
                }
        
        # build graph
        for i in range(n-1):
            word1, word2 = words[i], words[i+1]
            
            if len(word1) > len(word2) and word1[:len(word2)] == word2:
                return ''
            
            for w1, w2 in zip(word1, word2):
                if w1 != w2:
                    if w2 not in graph[w1]['children']:
                        total_edges += 1
                        graph[w1]['children'].add(w2)
                        graph[w2]['parents'] += 1
                    break
        
        # init - topological sort
        que = collections.deque()
        for w in graph.keys():
            if graph[w]['parents'] == 0:
                que.append(w)
        
        # loop - topological sort
        ans = ''
        while que:
            w = que.popleft()
            
            ans += w
            
            for child in graph[w]['children']:
                graph[child]['parents'] -= 1
                remove_edges += 1
                
                if graph[child]['parents'] == 0:
                    que.append(child)
        
        return ans if total_edges == remove_edges else ''
            
