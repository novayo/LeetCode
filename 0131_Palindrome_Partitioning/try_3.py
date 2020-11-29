class Solution:
    def partition(self, s: str) -> List[List[str]]:
        '''
        backtracking + dp
        '''
        
        ans = []
        dp = collections.defaultdict(bool)
        
        
        def isPalindrome(start, end):
            end -= 1
            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True
        
        
        def backtracking(start, curList):
            if start >= len(s):
                ans.append(curList[:])
                return
            
            for end in range(start, len(s)):
                if s[end] == s[start] and (end-start <= 2 or dp[start+1, end-1] == True):
                    dp[start, end] = True
                    curList.append(s[start:end+1])
                    backtracking(end+1, curList)
                    curList.pop()
        
        backtracking(0, [])
        return ans
