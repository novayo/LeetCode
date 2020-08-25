class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # set
        '''
        用set，去紀錄已經找過得並查詢
        時間複雜度：O(n)
        空間複雜度：O(n)
        '''
        
        found = set()
        for num in nums:
            if num in found:
                return num
            else:
                found.add(num)
