class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        '''
        3 => 1插在b2中間
        4 => 2插在b2中間
        5 => 1插在b4中間
        6 => 2插在b4中間
        '''
        ans = []
        one_list = ['0', '1', '8']
        two_list = ['11', '69', '88', '96']
        
        buffer = two_list.copy()
        for i in range(3, n+1):
            ans.clear()
            length = (i-1) // 2
            
            if i&1 == 1:
                for s in one_list:
                    for string in buffer:
                        ans.append(string[:length] + s + string[length:])
            else:
                for s in two_list + ['00']:
                    for string in buffer:
                        ans.append(string[:length] + s + string[length:])
                buffer = ans.copy()
            
        if n == 1:
            return one_list
        elif n == 2:
            return two_list
        else:
            return ans
