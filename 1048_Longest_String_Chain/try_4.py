import collections

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        word_by_len = collections.defaultdict(list)
        for word in words:
            word_by_len[len(word)].append(word)
        
        
        dp = collections.defaultdict(int)
        for length in sorted(word_by_len.keys(), reverse=True):
            
            for word in word_by_len[length]:
                if word not in dp:
                    dp[word] = 1
                
                for next_word in word_by_len[length+1]:
                    i = j = diff_counter = 0
                    isValid = True
                    while i < len(word):
                        if word[i] == next_word[j]:
                            i, j = i+1, j+1
                        elif diff_counter == 0:
                            diff_counter += 1
                            j += 1
                        else:
                            isValid = False
                            break
                    
                    if isValid:
                        dp[word] = max(dp[word], dp[next_word] + 1)
        return max(dp.values())
