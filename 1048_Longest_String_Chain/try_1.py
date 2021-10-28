class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        ans = 0
        found = set()
        words_set = set(words)
        words.sort(key=len)

        for i in range(len(words)-1, -1, -1):
            word = words[i]
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