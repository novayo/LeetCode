class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        # Kadane's algorithm : https://www.youtube.com/watch?v=86CQq3pKSUw
        
        def Kadane(A):
            cur_max = max_sum = A[0]
            cur_min = min_sum = A[0]
            sum = A[0]
            for i in range(1, len(A)):
                cur_max = max(A[i], cur_max + A[i])
                max_sum = max(max_sum, cur_max)
                cur_min = min(A[i], cur_min + A[i])
                min_sum = min(min_sum, cur_min)
                sum += A[i]
            return max(max_sum, sum-min_sum) if max_sum > 0 else max_sum
        
        return Kadane(A)
