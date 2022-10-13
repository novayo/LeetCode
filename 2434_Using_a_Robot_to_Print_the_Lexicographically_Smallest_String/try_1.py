from sortedcontainers import SortedList

class Solution:
    def robotWithString(self, s: str) -> str:
        
        bst = SortedList([ch for ch in s])

        ans = ""
        stack = []
        for ch in s:
            smallest = bst[0]

            while stack and stack[-1] <= smallest:
                ans += stack.pop()
            
            if ch == smallest:
                ans += ch
            else:
                stack.append(ch)
            bst.remove(ch)
                
        ans += "".join(stack[::-1])
        return ans