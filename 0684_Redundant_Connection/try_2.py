class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # build graph
        graph = collections.defaultdict(set)
        for i, j in edges:
            graph[i].add(j)
            graph[j].add(i)
        
        
        def find_cycle(node, parent, found=set()):
            nonlocal cycle, in_cycle
            if node in found:
                in_cycle = True
                cycle.add(node)
                return True
            
            found.add(node)
            for child in graph[node]:
                if parent == child:
                    continue
                
                if find_cycle(child, node, found):
                    if in_cycle:
                        if node not in cycle:
                            cycle.add(node)
                            cycle.add((child, node))
                            cycle.add((node, child))
                        else:
                            cycle.add((child, node))
                            cycle.add((node, child))
                            in_cycle = False
                    
                    return True
            found.remove(node)
        
        cycle = set()
        in_cycle = True
        find_cycle(1, None, set())
        
        for i, j in edges[::-1]:
            if (i, j) in cycle:
                return i, j

