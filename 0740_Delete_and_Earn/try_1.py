class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        nums.sort()
        
        counter = [1]
        index = {nums[0]: 0}
        numbers = [nums[0]]
        pre = nums[0]
        for num in nums[1:]:
            if pre == num:
                counter[-1] += 1
            else:
                counter.append(1)
                index[num] = len(counter)-1
                numbers.append(num)
                pre = num
        
        ans = 0
        dp = [0] * len(numbers)
        for i in range(len(numbers)-1, -1, -1):
            tmp = 0
            for j in range(i+1, len(numbers)):
                if numbers[i] + 1 != numbers[j]:
                    tmp = max(tmp, dp[j])
            dp[i] = counter[i] * numbers[i] + tmp
            ans = max(ans, dp[i])
            
        return ans
