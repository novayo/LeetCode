class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(a, b):
            return int(b+a) - int(a+b)
        
        nums = sorted([str(x) for x in nums], key=functools.cmp_to_key(compare))
        return ''.join(nums) if nums[0] != '0' else '0'
        