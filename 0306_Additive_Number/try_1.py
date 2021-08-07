class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        if len(num) < 3:
            return False
        
        for word1_len in range(1, len(num)):
            for word2_len in range(1, len(num)):
                
                if max(word1_len, word2_len) > len(num) - word1_len - word2_len:
                    break
                    
                start_index = word1_len + word2_len
                
                if word1_len > 1 and num[:word1_len][0] == '0' or \
                   word2_len > 1 and num[word1_len: start_index][0] == '0':
                    continue
                
                dp = [int(num[:word1_len]), int(num[word1_len: start_index])]

                found_end = True
                while start_index < len(num):
                    next_word = str(dp[0] + dp[1])
                    if num[start_index : start_index + len(next_word)] == next_word:
                        dp = [dp[1], dp[0] + dp[1]]
                        start_index += len(next_word)
                    else:
                        found_end = False
                        break
                
                if found_end:
                    return True
                
        return False
