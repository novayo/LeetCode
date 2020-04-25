class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 如果沒有0，一定能到尾端
        # 如果有0，則去看那個index前面有沒有能不能超過他，如果可以就能到尾端
        
        # 找 0 index
        zeros = []
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros.append(i)
        
        if not zeros or len(nums) == 1:
            return True
        
        if zeros[0] == 0:
            return False
        else:
            zeros.insert(0,0)
        
        for i in range(1, len(zeros)):
            index = zeros[i]
            count = 1
            flag = True
            while index > 0:
                index -= 1
                if nums[index] > count or (zeros[i] == len(nums)-1 and nums[index] >= count):
                    flag = False
                    break
                count += 1
            if flag:
                return False
        return True
