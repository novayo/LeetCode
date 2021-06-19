class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        ans = []
        def recr(left_num, right_num, cur_str=""):
            nonlocal ans
            
            if left_num == right_num == 0:
                ans.append(cur_str)
                return
            
            if 0 < left_num < right_num:
                recr(left_num-1, right_num, cur_str+"(")
                recr(left_num, right_num-1, cur_str+")")
            elif left_num == right_num:
                recr(left_num-1, right_num, cur_str+"(")
            elif left_num == 0:
                recr(left_num, right_num-1, cur_str+")")
        
        recr(n, n, "")
        return ans