class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def get_dist(current_code: str) -> int:
            dist = 0
            for i in range(4):
                _dist = abs(int(current_code[i])- int(target[i]))
                dist += min(_dist, 10-_dist)
            return dist
        
        start_code = "0000"
        deadends = set(deadends)
        pq = [(get_dist(start_code) + 0, 0, start_code)] # score, step, current_code
        
        # init
        if start_code in deadends:
            return -1
        deadends.add(start_code)
        
        # dijkstra
        while pq:
            score, step, code = heapq.heappop(pq)
            if code == target:
                return step
            
            for i in range(4):
                c = int(code[i])
                
                # Turn right
                for _c in [c+1 if c != 9 else 0, c-1 if c != 0 else 9]:
                    new_code = code[:i] + str(_c) + code[i+1:]
                    if new_code not in deadends:
                        heapq.heappush(pq, (get_dist(new_code) + step + 1, step+1, new_code))
                        deadends.add(new_code)
                
        return -1
                
