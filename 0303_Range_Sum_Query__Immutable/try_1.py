class NumArray:

    def __init__(self, nums: List[int]):
        '''
        累加起來，這樣dp[i]-dp[j]就代表i加到j的總和
        '''
        self.dp = [0]
        
        # 累加
        for n in nums:
            self.dp.append(self.dp[-1] + n)

    def sumRange(self, i: int, j: int) -> int:
        return self.dp[j+1]-self.dp[i]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)