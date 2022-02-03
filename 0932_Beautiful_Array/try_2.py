class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        '''
        odd 放左邊
        even 放右邊
        '''
        
        ans = [1]
        while len(ans) < n:
            tmp = []
            for a in ans:
                tmp.append(2*a-1)
            for a in ans:
                tmp.append(2*a)
            ans = tmp
        
        return [a for a in ans if a <= n]
        
