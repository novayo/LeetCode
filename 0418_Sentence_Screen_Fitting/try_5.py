class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        s = ' '.join(sentence) + ' '
        n = len(s)
        i = 0
        
        for _ in range(rows):
            i += cols
            while i > 0 and s[i%n] != ' ':
                i -= 1
            i += 1
        
        return i // n
