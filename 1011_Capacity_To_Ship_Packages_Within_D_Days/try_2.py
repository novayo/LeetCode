class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        # binary search
        if D == len(weights):
            return max(weights)
        left, right = max(weights), sum(weights)
        
        while left <= right:
            mid = (left + right) // 2
            if self.calculate_D(weights, mid) <= D:
                right = mid - 1
            else:
                left = mid + 1
        return left
        
    def calculate_D(self, weights, W):
        rt = tmp = 0
        for w in weights:
            tmp += w
            if tmp > W:
                rt += 1
                tmp = w
            elif tmp == W:
                rt += 1
                tmp = 0

        return rt + (tmp != 0)
