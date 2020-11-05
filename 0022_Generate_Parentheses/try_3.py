class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        queue = collections.deque()
        queue.append((n, n, ""))
        
        while queue:
            left, right, string = queue.popleft()
            
            if left == right == 0:
                ans.append(string)
                continue
            
            # 放左邊
            if left > 0:
                queue.append((left-1, right, string+"("))
            
            # 放右邊
            if 0 <= left <= right-1:
                queue.append((left, right-1, string+")"))
        
        return ans
