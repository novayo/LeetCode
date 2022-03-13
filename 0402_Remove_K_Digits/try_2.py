class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        _k = k
        min_stack = []
        
        for n in num:
            while min_stack and _k > 0 and min_stack[-1] > n:
                min_stack.pop()
                _k -= 1
            min_stack.append(n)
        
        
        min_stack = min_stack[:len(num)-k]
        if not min_stack:
            return '0'
        else:
            return str(int(''.join(min_stack)))