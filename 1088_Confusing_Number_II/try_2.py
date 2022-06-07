class Solution:
    def confusingNumberII(self, n: int) -> int:
        pair = {0:0,1:1,6:9,8:8,9:6}
        
        # init
        ans = 0
        found = set()
        queue = set()
        for key, val in pair.items():
            if key != 0:
                queue.add((key, val, 10))
                found.add((key, val, 10))
        
        while queue:
            num, rot_num, unit = queue.pop()
            
            if num != rot_num:
                ans += 1
            
            for key, val in pair.items():
                if key == 0 and num == 0:
                    continue
                
                if num*10 + key > n:
                    continue
                
                p = (num*10 + key, val * unit + rot_num, unit*10)
                if p in found:
                    continue
                
                queue.add(p)
                found.add(p)
            
        return ans