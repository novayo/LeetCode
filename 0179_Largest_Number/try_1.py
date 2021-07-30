class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # 比較誰組成大，就排前面
        def compare(item1, item2):
            return int(item2+item1) - int(item1+item2)
        
        for i in range(len(nums)):
            nums[i] = str(nums[i])
        
        nums.sort(key=functools.cmp_to_key(compare))
        return ''.join(nums) if nums[0] != '0' else '0'
