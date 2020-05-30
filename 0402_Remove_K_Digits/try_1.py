class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) <= k:
            return '0'
        
        ans = ""
        ans_len = len(num) - k
        index = 0
        
        while ans_len > 0:
            tmp = 'a'
            min_index = index
            for i in range(index, len(num)-ans_len+1):
                if num[i] < tmp:
                    tmp = num[i]
                    min_index = i
            
            ans += num[min_index]
            index = min_index+1
            ans_len-=1
        
        return str(int(ans))
