class Solution:
    def countSubstrings(self, s: str) -> int:
        '''
        LPS => 'a#b#b#a'
            =>  when getting answer, 
                => if we encounter #, the answer would plus LPS[i]//2
                => if we encounter a, the answer would plus (LPS[i]+1)//2
        '''
        
        new_s = '#' + '#'.join(s) + '#'
        
        n = len(new_s)
        center = 1
        center_right = 2
        
        LPS = [0] * n
        
        lps_max_index = 0
        lps_max_length = 0
        
        for current_right in range(n):
            # use left answer
            if current_right < center_right:
                current_left = 2*center - current_right
                LPS[current_right] = min(LPS[current_left], center_right-current_right)
            
            # calculate current_right LPS
            left = current_right - LPS[current_right] - 1
            right = current_right + LPS[current_right] + 1
            while left >= 0 and right < n and new_s[left] == new_s[right]:
                LPS[current_right] += 1
                left = current_right - LPS[current_right] - 1
                right = current_right + LPS[current_right] + 1
            
            
            # update answer
            if LPS[current_right] > lps_max_length:
                lps_max_length = LPS[current_right]
                lps_max_index = current_right
            
            # update center_right
            if current_right + LPS[current_right] >= center_right:
                center = current_right
                center_right = current_right + LPS[current_right]
        
        # start_index = (lps_max_index - lps_max_length) // 2
        # print(s[start_index: start_index+lps_max_length])
        
        ans = 0
        for i, _s in enumerate(new_s):
            if _s == '#':
                ans += LPS[i] // 2
            else:
                ans += (LPS[i]+1)//2
        return ans
                
        