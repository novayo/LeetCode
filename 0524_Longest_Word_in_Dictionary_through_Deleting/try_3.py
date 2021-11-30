class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        '''
        1. sort dictionary by length and do KMP 
            => O(len(s) * n + nlogn) n for len(dictionary)
        *2. do bfs to delete one char in every layer and find in dictionary(list to set) 
            => O(len(s)^2)
        '''
        dictionary = set(dictionary)
        
        if s in dictionary:
            return s
        
        buffer = set([s])
        
        while buffer:
            possible = []
            tmp_buffer = set()
            
            while buffer:
                string = buffer.pop()
                
                for i in range(len(string)):
                    # delete one char
                    target = string[:i] + string[i+1:]
                    
                    if target in dictionary:
                        possible.append(target)
                    
                    tmp_buffer.add(target)
            
            if possible:
                return sorted(possible)[0]
            
            buffer = tmp_buffer
        
        return ""
