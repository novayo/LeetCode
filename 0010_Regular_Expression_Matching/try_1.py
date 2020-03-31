class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        queue = collections.deque()
        queue.append((0,0))
        
        while queue:
            sindex, pindex = queue.popleft()
            
            if sindex >= len(s) and pindex >= len(p):
                return True
            
            if sindex >= len(s):
                # 看p剩下的是不是為空白
                if pindex+1 < len(p) and p[pindex+1] == "*":
                    # 都不補
                    queue.append((sindex, pindex+2))
            elif pindex >= len(p):
                pass
            else:
                if pindex+1 < len(p) and p[pindex+1] == "*":
                    # 都不補
                    queue.append((sindex, pindex+2))

                    # 補到沒有p[pindex]
                    while sindex < len(s) and (s[sindex] == p[pindex] or p[pindex] == "."):
                        queue.append((sindex+1, pindex+2))
                        sindex += 1

                elif s[sindex] == p[pindex] or p[pindex] == ".":
                    queue.append((sindex+1, pindex+1))
                
        return False
