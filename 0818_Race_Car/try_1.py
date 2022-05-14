class Solution:
    def racecar(self, target: int) -> int:
        ans = 0
        memo = set()
        queue = []
        queue.append((0, 1))
        
        while queue:
            next_q = []
            
            for pos, spd in queue:
                if pos == target:
                    return ans
                
                for p, s in [(pos+spd, spd*2), (pos, -1 if spd > 0 else 1)]:
                    if (p, s) in memo:
                        continue
                    if p < 0:
                        continue
                    next_q.append((p, s))
                    memo.add((p, s))
            
            ans += 1
            queue = next_q
        
        return -1