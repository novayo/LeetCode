class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        counter = collections.Counter()
        ans = i = 0
        
        for j, _s in enumerate(s):
            counter[_s] += 1
            
            cur_length = j-i+1
            leading_char = max(counter, key=counter.get)
            need_k =  cur_length - counter[leading_char]
            
            while i <= j and need_k > k:
                counter[s[i]] -= 1
                i += 1
                cur_length = j-i+1
                leading_char = max(counter, key=counter.get)
                need_k =  cur_length - counter[leading_char]
                
            ans = max(ans, j-i+1)
        
        return ans