class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        
        def backtracking(leftNum, rightNum, curString):
            nonlocal ans
            
            if leftNum > n or rightNum > n:
                return
            if leftNum == n and rightNum == n:
                ans.append(curString)
            
            if leftNum < rightNum:
                return
            elif leftNum == rightNum:
                backtracking(leftNum+1, rightNum, curString + '(')
            else:
                backtracking(leftNum+1, rightNum, curString + '(')
                backtracking(leftNum, rightNum+1, curString + ')')
        
        backtracking(0, 0, "")
        return ans
