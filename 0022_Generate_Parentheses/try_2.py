class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def recursive(left, right, string, ans):
            if left == right == 0:
                ans.append(string)
                return
            
            if 0 <= left <= right:
                recursive(left-1, right, string+"(", ans)
                recursive(left, right-1, string+")", ans)
        
        ans = []
        recursive(n, n, "", ans)
        return ans
