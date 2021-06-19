# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        # total= 0
        # for _ in range(100000):
        #     count = 0
        #     for i in range(8):
        #         count += 1 if rand7() <= 6 else 0
        #     total += 1 if count >= 8 else 0
        # print(total / 100000)
        
        # 模擬30%
        count = 0
        for i in range(8):
            count += 1 if rand7() <= 6 else 0
            
        is_1_to_3 = True if count >= 8 else False
        
        if is_1_to_3:
            # 去除多一個1的機率，使得每個數字機率 = 1/10
            tmp = rand7()
            while tmp == 7:
                tmp = rand7()
            return tmp % 3 + 1
        else:
            return rand7() + 3