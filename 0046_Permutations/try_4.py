class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        found = set()
        ans = []
        
        def recr(cur_list):
            if len(cur_list) == length:
                ans.append(cur_list[:])
                return
            
            for i in range(length):
                if i in found:
                    continue
                
                found.add(i)
                cur_list.append(nums[i])
                recr(cur_list)
                found.remove(i)
                cur_list.pop()
        
        recr([])
        return ans
