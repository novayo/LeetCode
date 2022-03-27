class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        
        def condition(speed):
            if speed == 0:
                return False
            total_hour = 0
            
            for d in dist[:-1]:
                total_hour += ceil(d / speed)
            total_hour += dist[-1] / speed
            
            return total_hour <= hour
        
        # binary search left
        ans = 0
        l, r = 1, 10**7
        while l <= r:
            mid = l + (r-l) // 2
            if condition(mid):
                ans = mid
                r = mid-1
            else:
                l = mid+1
        
        return ans if condition(ans) else -1