class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        '''
        往左邊多少格會找到略小 => left[i]
        往右邊多少格會找到略小 => right[i]
        此點的影響範圍 => arr[i] * left[i] * right[i]
        
        重複的值: 讓一邊不包含，另一邊包含
        '''
        MOD = 10 ** 9 + 7
        n = len(arr)
        left = [i for i in range(1, n+1)]
        right = [i for i in range(n, 0, -1)]
        
        # left
        stack = [] # [val, index]
        for i in range(n-1, -1, -1):
            while stack and arr[i] <= stack[-1][0]:
                val, index = stack.pop()
                left[index] = index - i
            stack.append((arr[i], i))
        
        # right
        stack = [] # [val, index]
        for i in range(n):
            while stack and arr[i] < stack[-1][0]:
                val, index = stack.pop()
                right[index] = i - index
            stack.append((arr[i], i))
        
        
        # get ans
        ans = 0
        for i, a in enumerate(arr):
            ans += a * left[i] * right[i]
            ans %= MOD
        return ans 
