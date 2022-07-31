class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        cur_length = 0
        cur_list = []
        for word in words:
            spaces = len(cur_list) - 1
            n = len(word)
            
            if not cur_list:
                cur_length += n
                cur_list.append(word)
            elif cur_length + (spaces+1) + n <= maxWidth:
                cur_length += n
                cur_list.append(word)
            else:
                ans.append(cur_list[0])
                if spaces == 0:
                    ans[-1] += ' ' * (maxWidth - len(ans[-1]))
                else:
                    base = (maxWidth - cur_length) // spaces
                    remain = (maxWidth - cur_length) % spaces

                    for s in cur_list[1:]:
                        ans[-1] += (' ' * (base + (remain > 0))) + s
                        remain -= 1
                
                cur_list = [word]
                cur_length = n
        
        ans.append(' '.join(cur_list))
        ans[-1] += ' ' * (maxWidth - len(ans[-1]))
        return ans