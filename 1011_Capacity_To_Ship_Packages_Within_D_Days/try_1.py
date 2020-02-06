class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        lower = sum(weights) // D
        if lower < max(weights):
            lower = max(weights)
        
        while True:
            if self.calculate_D(weights, lower) <= D:
                return lower
            lower += 1
        
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
