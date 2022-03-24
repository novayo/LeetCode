class Solution:
    def magicalString(self, n: int) -> int:
        if n <= 3:
            return 1
        
        ans = 1
        put_1 = True
        a = [1,2,2]
        
        for i in range(2, n):   
            if put_1:
                for _ in range(a[i]):
                    a.append(1)
                    ans += 1
                    if len(a) >= n:
                        break
            else:
                a += [2] * a[i]
            
            if len(a) >= n:
                break
            
            put_1 = not put_1
        
        return ans