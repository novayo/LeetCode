class Solution:
    def minCut(self, s: str) -> int:
        '''
        dp: dp[j] = s[:j]要切幾個是回文 (沒有包含s[j]喔！是s[i~j-1])
        
            如果s[i:j]是回文，那s[i:j] = s[:j]最多會是 s[:i]+1 => dp[j] = min(dp[j], dp[i]+1)
            所以要去測試從每個i開始，往後的每個子字串（兩個for）
            
            因為第一個是0，所以dp[j] = dp[i-1]時，在j=0時會去比較0~-1（最後）
            若真的不用切，dp預設為0的話，會變成0+1 = 1，不符合答案
            所以dp要比s還要長，預設為-1~len(s)-1(也是最差的情況，每個都要切)
        '''
        if s == s[::-1]: return 0
        for i in range(1, len(s)):
            if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]:
                return 1
        
        
        def isPalindrome(string):
            i = 0
            j = len(string)-1
            while i<j:
                if string[i] != string[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        
        dp = [i for i in range(-1, len(s))]
        
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                if isPalindrome(s[i:j]):
                    dp[j] = min(dp[j], dp[i] + 1)
        
        return dp[-1]
