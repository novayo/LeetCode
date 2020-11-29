class Solution:
    def partition(self, s: str) -> List[List[str]]:
        '''
        backtracking + dp
        '''
        
        ans = []
        
        
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
            
            for i in range(start+1, len(s)+1):
                if isPalindrome(start, i):
                    curList.append(s[start:i])
                    backtracking(i, curList)
                    curList.pop()
        
        backtracking(0, [])
        return ans
