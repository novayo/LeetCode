
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        '''
        guess the distance => and count _m
        '''
        def condition(dist):
            ans, start = 1, position[0]
            for i in range(1, len(position)):
                if position[i] - start >= dist:
                    start = position[i]
                    ans += 1
            return ans
        
        position.sort()
        ans = -1
        l, r = 0, position[-1]-position[0]
        while l <= r:
            mid = l + (r-l) // 2
            guess = condition(mid)
            
            if guess == m:
                ans = mid
                l = mid+1
            elif guess < m:
                r = mid-1
            else:
                l = mid+1
        
        return ans if ans > -1 else l-1
