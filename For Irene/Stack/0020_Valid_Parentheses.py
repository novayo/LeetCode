class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for _s in s:
            if _s in '([{':
                stack.append(_s)
                continue
            
            # 右半邊
            if not stack:
                return False
            
            # 檢查是否配對
            left = stack.pop()
            if (_s == ')' and left != '(') \
               or (_s == ']' and left != '[') \
               or (_s == '}' and left != '{'):
                return False
        
        # 配對完之後，不應該有剩餘
        return len(stack) == 0