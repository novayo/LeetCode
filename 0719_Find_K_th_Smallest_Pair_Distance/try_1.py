class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        # binary search
        '''
        用答案去測試符合的k
        換句話說 要知道有幾個距離會小於 guess_distance
        之後去看看 這個個數是否有 <= k即可
        
        但要算有幾個距離不好算
        1.
        直接n^2爆開
        
        2.
        先sort (nlogn)
        
        1,1,2,3,4,5,8 
        guess_distance = 1
        
        由於是要算有幾個距離小於guess_distance
        因此就用一個當左，一個當右，當右-左 < guess_distance 就讓左+1直到不符合
        之後再把(右-左)累加就行，之後讓右+1再繼續測試
        
        範圍就是從 0~nums[-1]-nums[0]（最大-最小）
        '''
        
        def condition(guess_distance):
            count = 0
            left = 0
            for right in range(len(nums)):
                while nums[right] - nums[left] > guess_distance:
                    left += 1
                count += right - left
            return count >= k
        
        nums.sort()
        left, right = 0, nums[-1]-nums[0]
        while left < right:
            mid = left + (right - left) // 2
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        return left
