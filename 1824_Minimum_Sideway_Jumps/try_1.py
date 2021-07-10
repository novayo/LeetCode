class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        ans = 0
        cur_pos = set()
        
        cur_pos.add(2)
        for i in range(len(obstacles)-1):
            next = i+1
            
            if obstacles[next] in cur_pos:
                cur_pos.remove(obstacles[next])
                
                if len(cur_pos) == 0:
                    ans += 1
                    
                    for attempt in range(1, 4):
                        if attempt == obstacles[next] or attempt == obstacles[i]:
                            continue
                        cur_pos.add(attempt)
        
        return ans
