class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        # sort
        ans = []
        
        for _l, _r in zip(l, r):
            tmp = sorted(nums[_l:_r+1])
            
            diff = tmp[1] - tmp[0]
            for i in range(1, len(tmp)):
                if tmp[i-1] + diff != tmp[i]:
                    ans.append(False)
                    break
                elif i == len(tmp)-1:
                    ans.append(True)
                
        return ans
