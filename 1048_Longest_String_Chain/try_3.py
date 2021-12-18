class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        '''
        a1, c1, c2, c3, c4, a2, a_3, a_4, a3, a4, a5
        '''
        
        ans = 0
        found = set()
        words_set = set(words)
        words.sort(key=len)

        for i in range(len(words)-1, -1, -1):
            word = words[i]
            if word in found:
                continue
            
            cur_max = 0
            
            queue = set()
            queue.add(word)
            while queue:
                cur_max += 1
                
                tmp = set()
                while queue:
                    w = queue.pop()
                    found.add(w)

                    for j in range(len(w)):
                        target = w[:j] + w[j+1:]

                        if target not in words_set or target in found:
                            continue

                        tmp.add(target)
                queue = tmp
            
            ans = max(ans, cur_max)
            
            if i <= ans:
                break

        return ans
