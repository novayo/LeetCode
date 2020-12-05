class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def recursive(left, right):
            if left == right == 0:
                return [""]
            
            if 0 <= left <= right:

                left_list = recursive(left-1, right)
                for i in range(len(left_list)):
                    left_list[i] = "(" + left_list[i]

                right_list = recursive(left, right-1)
                for i in range(len(right_list)):
                    right_list[i] = ")" + right_list[i]

                return left_list + right_list
            
            else:
                return []
            
            
        return recursive(n, n)
