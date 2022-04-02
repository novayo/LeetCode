class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        '''
        '(' => push
        ')' => if top is '(' => pop & push 1
            => if top is A => add up all the A at the top => and double up the score
        '''
        ans = 0
        stack = []
        
        for _s in s:
            if _s == '(':
                stack.append(_s)
            else:
                if stack[-1] == '(':
                    stack[-1] = 1
                else:
                    add = 0
                    while stack[-1] != '(':
                        add += stack.pop()
                    stack[-1] = add * 2
        return sum(stack)
        
