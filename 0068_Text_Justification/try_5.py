class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        cur_list = []
        cur_word_length = 0
        
        for word in words:
            slots = len(cur_list) - 1
            
            if slots == -1:
                cur_list.append(word)
                cur_word_length += len(word)
            elif cur_word_length + slots + len(word) + 1 <= maxWidth:
                cur_list.append(word)
                cur_word_length += len(word)
            else:
                ans.append('')
                
                if slots == 0:
                    ans[-1] += cur_list[0] + ' ' * (maxWidth - cur_word_length)
                else:
                    space = (maxWidth - cur_word_length) // slots
                    remain = (maxWidth - cur_word_length) % slots
                    
                    for string in cur_list[:-1]:
                        ans[-1] += string + ' ' * (space + (remain > 0))
                        remain -= 1
                    ans[-1] += cur_list[-1]
                    
                cur_list = [word]
                cur_word_length = len(word)
        
        ans.append(' '.join(cur_list))
        ans[-1] += ' ' * (maxWidth - len(ans[-1]))
        return ans