class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        s = ' '.join(sentence) + ' '
        
        '''
        "a b c "
         
        '''
        n = len(s)
        idx = 0
        
        for i in range(rows):
            idx += cols
            
            if s[idx % n] == ' ':
                idx += 1
            else:
                while idx > 0 and s[(idx-1)%n] != ' ':
                    idx -= 1
        return idx // n
