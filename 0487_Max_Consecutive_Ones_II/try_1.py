class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # two pass
        '''
        先掃過一次，去紀錄值的個數
        先預設第一個為1，之後0101去排
        
        之後掃第二次，看看哪個x+1+y最大
        '''
        
        count = []
        is_one_turn = True
        
        if nums[0] == 0:
            is_one_turn = False
            count.append(0)
        
        # first loop
        tmp = 0 
        for num in nums:
            if is_one_turn:
                if num == 0:
                    is_one_turn = False
                    count.append(tmp)
                    tmp = 1
                    continue
                else:
                    tmp += 1
            else:
                if num == 1:
                    is_one_turn = True
                    count.append(tmp)
                    tmp = 1
                    continue
                else:
                    tmp += 1
        
        count.append(tmp)
        # second loop
        ans = 0
        for i in range(0, len(count), 2):
            tmp1 = count[i]
            tmp2 = count[i] + 1 if i - 1 >= 0 or i + 1 < len(count) else 0
            tmp3 = count[i] + 1 + count[i+2] if i + 2 < len(count) and count[i+1] == 1 else 0
            ans = max(ans, tmp1, tmp2, tmp3)
        return ans
            
            
