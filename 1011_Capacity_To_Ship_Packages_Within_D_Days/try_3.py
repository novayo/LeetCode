class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def condition(guess_weight):
            ret_day = loading = 0
            for w in weights:
                loading += w
                if loading > guess_weight:
                    loading = w
                    ret_day += 1
            
            if loading > 0:
                ret_day += 1
            return ret_day <= days
        
        
        ans = 1
        l, r = max(weights), sum(weights)
        while l <= r:
            mid = l + (r-l) // 2
            if condition(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans
