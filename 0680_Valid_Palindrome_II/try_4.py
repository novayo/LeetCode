class Solution:
    def validPalindrome(self, s: str) -> bool:
        # 確認是不是回文 => 去檢查文字反過來後還有沒有跟原本一樣 => s == s[::-1]
        # 但我們不想每個(i, j)都反過來檢查一次，太慢 (反過來的時間複雜度=O(n))
        # 所以，我們檢查頭尾，如果不吻合，就看要刪除i (s[i+1:j+1])，還是刪除j (s[i:j])
        # 因為只能刪除一次，所以只需檢查這兩次即可
        i, j = 0, len(s) - 1
        
        while i < j:
            if s[i] == s[j]:
                i, j = i+1, j-1
            elif s[i:j] == s[i:j][::-1] or \
                 s[i+1:j+1] == s[i+1:j+1][::-1]:
                return True
            else:
                return False
        
        return True

