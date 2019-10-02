class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding Window: Learning from https://www.youtube.com/watch?v=mtHelVTLKRQ&t=6m15s
        left, right, ans, _set = 0, 0, 0, set()
        while left < len(s) and right < len(s):
            if s[right] in _set:
                _set.remove(s[left])
                left += 1
            else:
                _set.add(s[right])
                right += 1
            ans = max(ans, right - left)
        return ans
