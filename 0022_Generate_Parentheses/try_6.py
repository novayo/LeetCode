class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        ans = []
        
        def recr(left_parentheses_count, right_parentheses_count, cur_string):
            nonlocal ans
            
            if left_parentheses_count > n or right_parentheses_count > n:
                return
            
            if left_parentheses_count == n and right_parentheses_count == n:
                ans.append(cur_string)
            
            if left_parentheses_count == right_parentheses_count:
                recr(left_parentheses_count+1, right_parentheses_count, cur_string + '(')
            else:
                recr(left_parentheses_count+1, right_parentheses_count, cur_string + '(')
                recr(left_parentheses_count, right_parentheses_count+1, cur_string + ')')
        
        recr(0, 0, '')
        return ans
