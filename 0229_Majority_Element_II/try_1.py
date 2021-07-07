class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # candidate 變形：最多兩個答案，所以計算兩個可能，再考慮個數即可
        count1, candidate1 = 0, None
        count2, candidate2 = 0, None
        
        for num in nums:
            # 判斷要擺在前面，因為candidate1有match了，此時的count2=0也不用更新
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 += 1
            elif count2 == 0:
                candidate2 = num
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        
        # 若長度為6，則可能沒有答案，或是candidate的個數沒有超過1/3
        # 因此需計算個數
        ans = []
        count1 = count2 = 0
        for num in nums:
            count1 += 1 if candidate1 == num else 0
            count2 += 1 if candidate2 == num else 0
        
        if count1 > len(nums)/3:
            ans.append(candidate1)
        if count2 > len(nums)/3:
            ans.append(candidate2)
        
        return ans
