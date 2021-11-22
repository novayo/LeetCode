class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        '''
        看有幾個符合，缺少的group要三個以上才能補齊
        '''
        
        def getString_Counter(s):
            shrink_sting = ''
            counter = []
            s += ' '
            i = 1
            while i < len(s):
                count = 1
                while i < len(s) and s[i] == s[i-1]:
                    i += 1
                    count += 1
                shrink_sting += s[i-1]
                counter.append(count)
                i += 1
            return shrink_sting, counter
        
        def isValid(counter1, counter2):
            if len(counter1) != len(counter2):
                return False
            
            for c1, c2 in zip(counter1, counter2):
                if (c1 == 2 and c2 == 1) or (c1 < c2):
                    return False
            return True
        
        
        
        # build counter and string
        result_s, result_c1 = getString_Counter(s)
        
        ans = 0
        for w in words:
            result_w, result_c2 = getString_Counter(w)
            
            if result_s == result_w and isValid(result_c1, result_c2):
                ans += 1
        return ans
        

