class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        counter = collections.Counter(nums)
        
        for num in sorted(nums):
            if counter[num] > 0:
                c = counter[num]
                for j in range(k):
                    counter[num+j] -= c
                    if counter[num+j] < 0:
                        return False
        
        return True
