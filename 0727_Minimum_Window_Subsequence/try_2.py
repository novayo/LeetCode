class Solution:
    def minWindow(self, S: str, T: str) -> str:
        ans = ""
        start = -1
        
        while True:
            findEnd = start
            
            # 找到從start開始的第一個符合的組合（用迴圈是因為要確認所有的T都有在要找的範圍裡面）
            for t in T:
                findEnd = S.find(t, findEnd + 1) # 為了不找到同樣的
                if findEnd == -1:
                    return ans
            findEnd += 1  # 因為findEnd是找到T[-1]在S的index（若要找"abc", 則findEnd剛好會是2），故+1
            
            # 從第一個符合的組合開始往回找，可以濾掉這種情況
            '''
            S = "aaaaaabc"   or   S = "aazzzabc"
            T = "aabc"       or   T = "aabc"
            
            start = -1
            findEnd = 7
            但我們只要aabc就好，不要S[start+1: findEnd] = "aaaaaabc" or "aazzzabc"
            
            因此從後面找回來，但要保證都有包含aabc，所以跟前面一樣，只是要用rfind找 + T要反著拿
            '''
            findStart = findEnd
            for t in reversed(T):
                findStart = S.rfind(t, start + 1, findStart) # 找start+1 ~ findStart-1
            
            # 更新答案
            if findEnd - findStart < len(ans) or len(ans) == 0:
                ans = S[findStart: findEnd]
                
            start = findStart + 1 # 更新start，往下一個點拿
