class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == '1':
            return False
        
        next_i = 0
        queue = collections.deque()
        
        queue.append(0)
        while queue:
            n = queue.popleft()
            
            if max(next_i, n+minJump) >= len(s):
                return False
            
            for i in range(max(next_i, n+minJump), n+maxJump+1):
                if i >= len(s)-1:
                    return True
                if s[i] == '0':
                    queue.append(i)
            
            next_i = max(next_i, n+maxJump+1)
        
        return False