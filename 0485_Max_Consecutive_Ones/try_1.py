class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        '''
        直接掃過去，是1就+1，是0就變成0，同時更新ans
        時間複雜度：O(n)
        空間複雜度：O(1)
        '''
        
        ans = 0
        count = 0
        for num in nums:
            if num == 0:
                count = 0
            else:
                count += 1
            ans = max(ans, count)
        return ans
