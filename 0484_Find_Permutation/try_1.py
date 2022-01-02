class Solution:
    def findPermutation(self, s: str) -> List[int]:
        '''
        III
        123
        
        DDD
        321
        
        DI
        123 -> 213
        
        IIDD
        12345 -> 1,2,5,4,3
        
        IDI
        1234 -> 1,3,2,4
        
        DDDID
        432165
        '''
        s += '#'
        ans = list(range(1, len(s)+1))
        
        cur_number = 0
        cur_string = ''
        count = 0
        for i in range(len(s)):
            if i == 0:
                cur_string += s[i]
                count = 1
            elif cur_string != s[i]:
                if cur_string == 'D':
                    ans[cur_number:cur_number+count+1] = ans[cur_number:cur_number+count+1][::-1]
                    
                cur_number += count
                cur_string = s[i]
                count = 1
            else:
                count += 1
        
        return ans
        
