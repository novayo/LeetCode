class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        # binary search
        left, right = 1, max(piles)
        
        while left <= right:
            mid = (left + right) // 2
            if self.calculate_H(piles, mid) <= H:
                right = mid - 1
            else:
                left = mid + 1
        return left
        
    def calculate_H(self, piles, K):
        rt = 0
        for pile in piles:
            rt += math.ceil(pile / K)
        return rt
