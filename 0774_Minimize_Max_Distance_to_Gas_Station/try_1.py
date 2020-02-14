class Solution:
    def minmaxGasDist(self, stations: List[int], K: int) -> float:
        # 用binary search去測試答案D
        def possible(D):
            return sum(math.ceil((stations[i+1] - stations[i]) / D) - 1 for i in range(len(stations)-1)) <= K

        left, right = 0, stations[-1] - stations[0]
        while right - left > 1e-6:
            mid = (left + right) / 2
            if possible(mid):
                right = mid
            else:
                left = mid
        return left
