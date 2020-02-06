class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        if len(piles) == H:
            return max(piles)
        lower = math.ceil(sum(piles) / H)
        
        while True:
            if self.calculate_H(piles, lower) <= H:
                return lower
            lower += 1
        
    def calculate_H(self, piles, K):
        rt = 0
        for pile in piles:
            rt += math.ceil(pile / K)
        return rt
