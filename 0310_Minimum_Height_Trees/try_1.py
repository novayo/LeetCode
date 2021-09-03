class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        '''
        為何是2個node?
        '''
        if n <= 2:
            return [i for i in range(n)]
        
        # build graph
        graph = collections.defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        
        # find leaves
        l_leaves = []
        for i in range(n):
            if len(graph[i]) == 1:
                l_leaves.append(i)
        
        # loop
        while n > 2:
            n -= len(l_leaves)
            new_leaves = []
            for leaf in l_leaves:
                parent_leaf = graph[leaf].pop()
                graph[parent_leaf].remove(leaf)
                if len(graph[parent_leaf]) == 1:
                    new_leaves.append(parent_leaf)
            l_leaves = new_leaves
        return l_leaves
