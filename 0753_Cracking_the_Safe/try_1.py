class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        '''
        最多k位數，然後ckeck n位數
        0123
        '''
        ans = '0' * n
        
        cache = set([ans])
        i = 0
        
        while True:
            all_in_set = True
            
            for _k in range(k-1, -1, -1):
                t = ans[i+1:] + str(_k)
                if t in cache:
                    continue
                
                all_in_set = False
                cache.add(t)
                ans += str(_k)
                i += 1
                break

            if all_in_set:
                break
            
        return ans
                
