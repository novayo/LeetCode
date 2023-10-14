class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        '''
        遇到1的時候+1，0的時候-1
        
        [....3........3.....]
        此時第一個3-第二個3之前就是 答案
        '''
        presum = [0]
        for num in nums:
            if num == 0:
                presum.append(presum[-1]-1)
            else:
                presum.append(presum[-1]+1)
        
        ans = 0
        visited = {}
        for j in range(len(presum)):
            if presum[j] in visited:
                ans = max(ans, j - visited[presum[j]])
            else:
                visited[presum[j]] = j
        return ans
        
