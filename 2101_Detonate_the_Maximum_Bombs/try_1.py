class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        def valid(p1, p2):
            return pow(p1[0]-p2[0], 2) + pow(p1[1]-p2[1], 2) <= pow(p1[2], 2)
        
        bombs = [tuple(bomb) for bomb in bombs]
        counter = collections.Counter(bombs)
        bombs = list(set(bombs))
        n = len(bombs)
        ans = 0
        
        for i in range(n):
            que = set([bombs[i]])
            found = set([bombs[i]])
            nodes = counter[bombs[i]]
            while que:
                next_que = set()
                
                for p1 in que:
                    for p2 in bombs:
                        if p2 in found:
                            continue
                        if valid(p1, p2):
                            next_que.add(p2)
                            found.add(p2)
                            nodes += counter[bombs[i]]
                que = next_que
            
            ans = max(ans, nodes)   
        return ans