class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        n = len(words)
        
        ans = []
        i = 0
        while i < n:
            length_only_char = cur_length = len(words[i])
            num_of_char = 1
            j = i+1
            while j < n and cur_length + len(words[j]) + 1 <= maxWidth:
                length_only_char += len(words[j])
                cur_length += len(words[j]) + 1
                num_of_char, j = num_of_char+1, j+1
            
            if j == n:
                s = ' '.join(words[i: j])
                s += ' ' * (maxWidth - len(s))
                ans.append(s)
                break
            
            # cacluate answer
            if num_of_char > 1:
                quotient = (maxWidth - length_only_char) // (num_of_char-1)
                remainder = (maxWidth - length_only_char) % (num_of_char-1)
                
                s = ''
                for k in range(num_of_char):
                    if k == 0:
                        s = words[i]
                    else:
                        s += ' ' * (quotient + (remainder > 0)) + words[i]
                        if remainder > 0: remainder -= 1
                    i += 1
                ans.append(s)
            else:
                s = words[i] + ' ' * (maxWidth - len(words[i]))
                ans.append(s)
                i += 1
            
        return ans