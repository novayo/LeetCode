class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        
        for asteroid in asteroids:
            if not ans:
                ans.append(asteroid)
                continue
            
            if asteroid > 0:
                ans.append(asteroid)
            else:
                # if new_left is bigger than before right
                while ans and ans[-1] > 0 and ans[-1] < abs(asteroid):
                    ans.pop()
                
                if ans and ans[-1] == abs(asteroid):
                    ans.pop()
                elif not ans or ans[-1] < 0:
                    ans.append(asteroid)
        
        return ans
