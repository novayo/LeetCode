class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        '''
        not valid: 2 4 5 6 7 9  
        valid: 0 1 8
        
        80 83 88
        '''
        nl, nh = len(low), len(high)
        low, high = int(low), int(high)
        ans = 0

        pair = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
        queue = collections.deque(['', '0', '1', '8'])
        while queue:
            s = queue.popleft()
            
            if (s == '0' or (s and s[0] != '0')) and low <= int(s) <= high:
                ans += 1
            
            for k, v in pair.items():
                t = k + s + v
                if int(t) > high or len(t) > nh:
                    continue
                queue.append(k+s+v)
        
        return ans
            
