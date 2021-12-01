class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        def find(string):
            a = b = c = float('inf')
            
            if len(string) < 2:
                return a, b, c
            
            for i in range(len(string)-1, 0, -1):
                target = string[i-1] + string[i]
                
                if target == r'//':
                    a = i-1
                elif target == r'/*':
                    b = i-1
                elif target == r'*/':
                    c = i-1
            return a, b, c
        
        def getString(string, i):
            if i + 2 >= len(string):
                return ''
            return string[i+2:]
        
        ans = []
        tmp = ''
        iscomment = False
        
        for string in source:
            while len(string) > 0:
                a, b, c = find(string)
                if iscomment == False and a < b:
                    tmp += string[:a]
                    string = ''
                elif iscomment == False and b < a:
                    iscomment = True
                    tmp += string[:b]
                    string = getString(string, b)
                elif iscomment == True and c != float('inf'):
                    iscomment = False
                    string = getString(string, c)
                elif iscomment == False:
                    tmp += string
                    string = ''
                else:
                    string = ''
            
            if iscomment == False and tmp != '':
                ans.append(tmp)
                tmp = ''
        
        return ans
                            
                    
