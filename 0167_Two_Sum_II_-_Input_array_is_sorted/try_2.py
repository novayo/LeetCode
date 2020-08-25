class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # binary search
        '''
        不是用index來跑binary search
        而是用sum來去尋找
        '''
        
        left, right = 0, len(numbers)-1
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum > target:
                right -= 1
            elif sum == target:
                return left+1, right+1
            else:
                left += 1
        
