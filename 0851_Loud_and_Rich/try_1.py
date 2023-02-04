class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        
        # init
        graph = {}
        for node in range(n):
            graph[node] = {'children': [], 'num_parent': 0}
        
        candidate_dict = {}
        for node in range(n):
            candidate_dict[node] = [quiet[node], node]
        
        # build graph
        for p, c in richer:
            graph[p]['children'].append(c)
            graph[c]['num_parent'] += 1
        
        # topological sort - init
        que = collections.deque()
        for node in range(n):
            if graph[node]['num_parent'] == 0:
                que.appendleft(node)
        
        # topological sort - get answer
        while que:
            node = que.pop()
            
            for c in graph[node]['children']:
                if candidate_dict[node][0] < candidate_dict[c][0]:
                    candidate_dict[c] = [candidate_dict[node][0], candidate_dict[node][1]]
                graph[c]['num_parent'] -= 1
                
                if graph[c]['num_parent'] == 0:
                    que.appendleft(c)
        
        # get answer
        return [candidate_dict[i][1] for i in range(n)]

