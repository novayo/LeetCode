# """
# This is GridMaster's API interface.
# You should not implement it, or speculate about its implementation
# """
#class GridMaster(object):
#    def canMove(self, direction: str) -> bool:
#        
#
#    def move(self, direction: str) -> bool:
#        
#
#    def isTarget(self) -> bool:
#        
#

class Solution(object):
    def findShortestPath(self, master: 'GridMaster') -> int:
        def getNextPos(i, j, dir):
            if dir == 'U':
                return [i-1, j]
            elif dir == 'D':
                return [i+1, j]
            elif dir == 'L':
                return [i, j-1]
            else:
                return [i, j+1]
        
        def getBackDir(dir):
            if dir == 'U':
                return 'D'
            elif dir == 'D':
                return 'U'
            elif dir == 'L':
                return 'R'
            else:
                return 'L'
        
        ans_pos = None
        
        graph = set()
        def backracking(i, j):
            nonlocal ans_pos, graph
            
            if master.isTarget():
                ans_pos = (i, j)
                return
            
            for dir in 'UDLR':
                x, y = getNextPos(i, j, dir)
                
                if (x, y) in graph:
                    continue
                
                if not master.canMove(dir):
                    continue
                
                master.move(dir)
                graph.add((x, y))
                backracking(x, y)
                master.move(getBackDir(dir))
        
        backracking(0, 0)
        
        if not ans_pos:
            return -1
        
        step = 0
        container = [(0, 0)]
        graph.remove((0, 0))
        while container:
            next_layer = []
            
            for i, j in container:
                
                if (i, j) == ans_pos:
                    return step
                
                for dir in 'UDLR':
                    x, y = getNextPos(i, j, dir)
                    if (x, y) not in graph:
                        continue
                    
                    next_layer.append((x, y))
                    graph.remove((x, y))
            
            container = next_layer
            step += 1
