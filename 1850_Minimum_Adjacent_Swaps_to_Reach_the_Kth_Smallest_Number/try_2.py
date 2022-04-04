class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        o_num = list(num)
        num = list(num)
        
        # find kth num
        for _ in range(k):
            i = len(num) - 1
            
            while i > 0 and num[i-1] >= num[i]:
                i -= 1
            i -= 1
            
            j = i+1
            while j < len(num) and num[j] > num[i]:
                j += 1
            j -= 1
            
            num[i], num[j] = num[j], num[i]
            num[i+1:] = num[i+1:][::-1]
        
        # 原本的跟後來的去比較，看要交換幾次就可以了
        ans = 0
        for i in range(len(num)):
            j = i
            while j < len(num) and num[i] != o_num[j]:
                j += 1
            
            ans += j-i
            o_num[i:j+1] = [o_num[j]] + o_num[i:j]
        return ans
