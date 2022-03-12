class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        queue = collections.deque(tokens)
        ans = score = 0
        
        while queue:
            while queue and power >= queue[0]:
                power -= queue.popleft()
                score += 1
              
            ans = max(ans, score)
            
            if score > 0 and queue:
                power += queue.pop()
                score -= 1
            else:
                break
        
        return ans
            
