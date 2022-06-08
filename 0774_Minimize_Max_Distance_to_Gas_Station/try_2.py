class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        def condition(guess):
            total_k = 0
            for i in range(n-1):
                d = stations[i+1]-stations[i]
                total_k += ceil(d / guess) - 1
            return total_k <= k
        
        
        n = len(stations)
        
        # find range of bs
        l = r = 0
        for i in range(n-1):
            r = max(r, stations[i+1]-stations[i])
        
        # bs
        offset = pow(10, -6)
        ans = float('inf')
        while r-l >= offset:
            mid = l + (r-l) / 2
            
            if condition(mid):
                ans = mid
                r = mid - offset
            else:
                l = mid + offset
        return ans