class Solution:
    def countAndSay(self, n: int) -> str:
        string = '1'
        
        for _ in range(n-1):
            next = ''
            
            i = 0
            s = ''
            counter = 0
                
            while i < len(string):
                if i == 0 or s == string[i]:
                    s = string[i]
                    counter += 1
                else:
                    next += str(counter) + s
                    counter = 1
                    s = string[i]
                i += 1
            
            next += str(counter) + s
            string = next
        
        return string
