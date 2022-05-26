
class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        ans = 0
        stack = []
        
        left_set = set(left)
        right_set = set(right)
        
        for i in range(n+1):
            if i not in left_set and i not in right_set:
                continue
            
            if i in left_set:
                if not stack:
                    ans = max(ans, i)
                else:
                    r_i = stack.pop()
                    mid = (i+r_i) / 2
                    
                    ans = max(ans, mid + mid - r_i, i-mid + n-mid)
            else:
                stack.append(i)
                
        if stack:
            ans = max(ans, n-stack[0])
        return int(ans)