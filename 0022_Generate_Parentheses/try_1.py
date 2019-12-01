class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = collections.deque()
        def recur(string, left, right):
            if left < 0 or right < 0: return
            if left == 0 and right != 0:
                recur(string + ")", left, right-1)
            elif left == 0 and right == 0:
                ans.append(string)
            else:
                if left == right:
                    recur(string + "(", left-1, right)
                elif left < right: 
                    recur(string + "(", left-1, right)
                    recur(string + ")", left, right-1)

        recur("", n, n)
        return ans
