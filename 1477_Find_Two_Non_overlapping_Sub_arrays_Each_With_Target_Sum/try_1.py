class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        left = [float('inf')] * n
        right = [float('inf')] * n
        
        cur_min = float('inf')
        i = j = cur_sum = 0
        while j < n:
            cur_sum += arr[j]
            
            while cur_sum > target:
                cur_sum -= arr[i]
                i += 1
            
            if cur_sum == target:
                cur_min = min(cur_min, j-i+1)
                cur_sum -= arr[i]
                i += 1
            
            left[j] = cur_min
            j += 1
        
        cur_min = float('inf')
        i = j = n-1
        cur_sum = 0
        while i >= 0:
            cur_sum += arr[i]
            
            while cur_sum > target:
                cur_sum -= arr[j]
                j -= 1
            
            if cur_sum == target:
                cur_min = min(cur_min, j-i+1)
                cur_sum -= arr[j]
                j -= 1
            
            right[i] = cur_min
            i -= 1
        
        ret = float('inf')
        for i in range(len(left)-1):
            ret = min(ret, left[i]+right[i+1])
        return ret if ret != float('inf') else -1

