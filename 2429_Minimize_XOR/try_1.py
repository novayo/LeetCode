class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        num_of_1 = collections.Counter(bin(num2)[2:])['1']
        
        ans = []
        for b in bin(num1)[2:]:
            if num_of_1 > 0 and b == '1':
                num_of_1 -= 1
                ans.append('1')
            else:
                ans.append('0')
        
        ans = ['0'] * (32 - len(ans)) + ans
        if num_of_1 > 0:
            for i in range(len(ans)-1, -1, -1):
                if num_of_1 == 0:
                    break
                if ans[i] == '0':
                    ans[i] = '1'
                    num_of_1 -= 1
        
        return int(''.join(ans), 2)