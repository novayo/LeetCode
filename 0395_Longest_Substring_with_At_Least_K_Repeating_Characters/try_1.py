class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        '''
        限定能出現的字母種類個數 => 從1開始
        '''
        ans = 0
        n = len(set(s))
        for length in range(1, n+1):
            times = [0] * 26
            l = r = k_cnt = alphabet_cnt = 0
            
            for r, _s in enumerate(s):
                i_time = ord(_s)-97
                times[i_time] += 1
                
                if times[i_time] == 1:
                    alphabet_cnt += 1
                if times[i_time] == k:
                    k_cnt += 1
                
                while l < r and alphabet_cnt > length:
                    j_time = ord(s[l])-97
                    
                    if times[j_time] == 1:
                        alphabet_cnt -= 1
                    if times[j_time] == k:
                        k_cnt -= 1
                    
                    times[j_time] -= 1
                    l += 1
                
                # 已經出現length次，且每個都>=k個
                if alphabet_cnt == length and k_cnt == length:
                    ans = max(ans, r-l+1)
        return ans
                
