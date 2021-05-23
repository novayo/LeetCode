class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        
        count = 0
        predict_space = 0
        text_length = 0
        text = []
        for word in words:
            if len(text) > 0:
                predict_space = 1
            
            next_length = count + predict_space + len(word)
            if next_length < maxWidth:
                count += predict_space + len(word)
                text_length += len(word)
                text.append(word)
            elif next_length == maxWidth:
                text.append(word)
                ans.append(' '.join(text))
                count = 0
                predict_space = 0
                text_length = 0
                text.clear()
            else:
                if len(text) == 1:
                    ans.append(text[0].ljust(maxWidth, ' '))
                else:
                    avg_spaces = (maxWidth - text_length) // (len(text)-1)  # 最少平均幾個空白
                    extra_spaces = (maxWidth - text_length) % (len(text)-1) # 有餘數的話，從左邊開始每個多補一個空白

                    tmp_ans = ''
                    for t in text[:-1]:
                        tmp_ans += t + ' '*avg_spaces
                        if extra_spaces > 0:
                            tmp_ans += ' '
                            extra_spaces -= 1
                    tmp_ans += text[-1]
                    ans.append(tmp_ans)
                count = len(word)
                text_length = len(word)
                text.clear()
                text.append(word)
        
        if len(text) > 0:
            ans.append(' '.join(text).ljust(maxWidth, ' '))
       
        return ans