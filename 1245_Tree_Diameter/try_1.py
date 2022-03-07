class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        if not edges:
            return 0
        
        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        ans = 0
        colored = set()
        def recr(node):
            nonlocal ans
            
            if all([x in colored for x in graph[node]]):
                return 1
            
            ret = []
            for child in graph[node]:
                if child not in colored:
                    colored.add(child)
                    ret.append(recr(child))
                    colored.remove(child)
            
            ret.sort(reverse=True)
            ans = max(ans, sum(ret[:2]))
            return ret[0] + 1
        
        start_node = edges[0][0]
        colored.add(start_node)
        recr(start_node)
        return ans