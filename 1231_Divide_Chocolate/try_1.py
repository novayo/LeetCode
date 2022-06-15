class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        # O(nlogn) time / O(1) space
        def condition(guess_ans, remain):
            cur_k = cur_sum = 0
            if cur_k >= k:
                return remain >= guess_ans
                
            for sweet in sweetness:
                cur_sum += sweet
                remain -= sweet
                if cur_sum >= guess_ans:
                    cur_k += 1
                    cur_sum = 0
                    
                    if cur_k >= k:
                        return remain >= guess_ans
            return False
        
        ans = 0
        _sum = sum(sweetness)
        l, r = min(sweetness), _sum
        while l <= r:
            mid = l + (r-l) // 2
            if condition(mid, _sum):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans