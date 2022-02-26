class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ans = ans_diff = float('inf')

        nums.sort()
        
        for i in range(n-2):
            for j in range(i+1, n-1):
                attempt = target - nums[i] - nums[j]
                
                index = bisect.bisect_left(nums, attempt, j+1)
                
                if index < n:
                    diff = abs(target - (nums[i] + nums[j] + nums[index]))
                    if diff < ans_diff:
                        ans_diff = diff
                        ans = (nums[i] + nums[j] + nums[index])
                
                if index-1 > j:
                    diff = abs(target - (nums[i] + nums[j] + nums[index-1]))
                    if diff < ans_diff:
                        ans_diff = diff
                        ans = (nums[i] + nums[j] + nums[index-1])
        
        return ans        
