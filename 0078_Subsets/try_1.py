class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # using gray code
        ans = []
        value = 1 << len(nums)
        for i in range(value):
            gray_code = i ^ i>>1
            tmp = []
            for i in range(len(nums)):
                if gray_code % 2 == 1:
                    tmp.append(nums[~i])
                gray_code //= 2
            ans.append(tmp)
        return ans
