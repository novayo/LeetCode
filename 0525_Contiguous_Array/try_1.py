class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        counter = 0
        maxlen = 0
        table = {0:-1} # 值，index
        
        for i in range(len(nums)):
            counter += 1 if nums[i] == 1 else -1
            if counter in table:
                maxlen = max(maxlen, i-table[counter])
            else:
                table[counter] = i
        return maxlen
