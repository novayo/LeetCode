class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        binary search
            1 ~ max(piles)
            condition => find hours by the speed
        '''
        
        def condition(speed):
            ret = 0
            for pile in piles:
                ret += math.ceil(pile / speed)
            return ret <= h
        
        ans = 0
        l, r = 1, max(piles)
        while l <= r:
            mid = l + (r-l) // 2
            if condition(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans
        
# Input: piles = [3,6,7,11], h = 8
# Output: 4
