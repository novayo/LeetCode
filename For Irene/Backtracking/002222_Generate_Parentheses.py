class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        
        def backtracking(left_num, right_num, cur_string):
            nonlocal ans
            
            if left_num < right_num or left_num > n:
                return
            
            if left_num == right_num == n:
                ans.append(cur_string)
                return
            
            backtracking(left_num+1, right_num, cur_string+'(')
            backtracking(left_num, right_num+1, cur_string+')')
        
        backtracking(0, 0, '')
        return ans