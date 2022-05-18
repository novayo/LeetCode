class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        cache = set([start])
        queue = set([start])
        layer = 0
        
        while queue:
            next_queue = set()
            
            for node in queue:
                
                if node == goal:
                    return layer
                
                for num in nums:
                    for t in [node+num, node-num, node^num]:
                        if t in cache:
                            continue
                        
                        if 0 <= t <= 1000:
                            cache.add(t)
                            next_queue.add(t)
                        else:
                            if t == goal:
                                return layer+1
            
            layer += 1
            queue = next_queue
        
        return -1
