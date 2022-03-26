class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        s = ' '.join(sentence) + ' '
        n = len(s)
        
        ans = 0
        remain = 0
        for i in range(rows):
            if remain < 0:
                ans += 1
            remain += cols
            ans += remain // n
            k = remain - (remain // n) * n
            while k >= 0 and s[k] != ' ':
                k -= 1
            k += 1
            remain = -(n - k)
            
            # 如果剛好放完
            if remain == 0:
                ans += 1
        
        return ans
