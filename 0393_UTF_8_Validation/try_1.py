class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        i = remain = 0
        flag = True
        
        while i < len(data):
            s = bin(data[i])[2:].zfill(8)
            
            if flag:
                if s[0] == '0':
                    pass
                elif s[:3] == '110':
                    remain = 1
                    flag = False
                elif s[:4] == '1110':
                    remain = 2
                    flag = False
                elif s[:5] == '11110':
                    remain = 3
                    flag = False
                else:
                    return False
            else:
                if s[:2] != '10':
                    return False
                remain -= 1
                if remain == 0:
                    flag = True
            i += 1
       
        return remain == 0
