class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        found = set()
        queue = []
        
        if '0000' in deadends:
            return -1
        
        queue.append('0000')
        found.add('0000')
        
        ans = 0
        while queue:
            tmp = []
            
            while queue:
                string = queue.pop()
                
                if string == target:
                    return ans
                
                for i in range(4):
                    int_string = int(string[i])
                    
                    offset_one = int_string + 1
                    offset_minus_one = int_string - 1
                    if offset_one > 9:
                        offset_one = 0
                    
                    if offset_minus_one < 0:
                        offset_minus_one = 9
                    
                    add_one = string[:i] + str(offset_one) + string[i+1:]
                    minus_one = string[:i] + str(offset_minus_one) + string[i+1:]
                    
                    if (add_one not in found) and (add_one not in deadends):
                        tmp.append(add_one)
                        found.add(add_one)
                    
                    if (minus_one not in found) and (minus_one not in deadends):
                        tmp.append(minus_one)
                        found.add(minus_one)
                        
            queue = tmp
            ans += 1
        
        return -1
        
        