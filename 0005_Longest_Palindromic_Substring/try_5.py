class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 加入#
        new_s = '#'
        for _s in s:
            new_s += _s + '#'
        
        
        n = len(new_s)
        LPS = [0] * n
        
        center = 1
        center_right = 2
        
        max_lps_length = 0
        max_lps_index = 0
        
        for current_right in range(1, n):
            # 先給current right初始值
            if current_right < center_right:
                current_left = center*2-current_right
                LPS[current_right] = min(LPS[current_left], center_right-current_right)
            
            # 以current right為中心的LPS (注意邊界)
            left = current_right - LPS[current_right] - 1
            right = current_right + LPS[current_right] + 1
            while left >= 0 and right < n and new_s[left] == new_s[right]:
                LPS[current_right] += 1
                left = current_right - LPS[current_right] - 1
                right = current_right + LPS[current_right] + 1
            
            # 更新答案
            if max_lps_length < LPS[current_right]:
                max_lps_length = LPS[current_right]
                max_lps_index = current_right
            
            # 更新center: 如果current right的右邊 >= center_right
            if current_right + LPS[current_right] >= center_right:
                center = current_right
                center_right = current_right + LPS[current_right]
        
        start_index = (max_lps_index - max_lps_length) // 2
        return s[start_index: start_index + max_lps_length]