class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        arr = sorted(zip(nums, cost))
        _min, _max = arr[0][0], arr[-1][0]
        
        n = len(arr)
        preSum = [arr[0][1]] * n
        for i in range(1, n):
            preSum[i] = preSum[i - 1] + arr[i][1]
            
        suffixSum = [arr[-1][1]] * n
        for i in range(n - 2, -1, -1):
            suffixSum[i] = suffixSum[i + 1] + arr[i][1]
            
        total = sum([_cost * (_num - _min) for _num, _cost in arr])
        ans = total
        for val in range(_min + 1, _max + 1):
            index = bisect.bisect_right(arr, (val, -1))
            total -= -preSum[index - 1] + suffixSum[index]
            ans = min(ans, total)
            
        return ans