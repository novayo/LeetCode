class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        table = collections.defaultdict(list)
        
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                table[i+j].append(nums[i][j])
        
        ans = []
        for i in range(len(table)):
            ans.extend(table[i][::-1])
        return ans
        
