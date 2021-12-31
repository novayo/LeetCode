class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # Kth smallest
        def quick_select(nums, target):
            
            if len(nums) == target:
                return max(nums)
            
            random_pick = random.choice(nums)
            
            less = []
            equals = 0
            larger = []
            
            for num in nums:
                if num == random_pick:
                    equals += 1
                elif num < random_pick:
                    less.append(num)
                else:
                    larger.append(num)
            
            if len(less) > target:
                return quick_select(less, target)
            elif len(less) + equals > target:
                return random_pick
            else:
                return quick_select(larger, target-len(less)-equals)
            
        return quick_select(nums, len(nums)-k)
