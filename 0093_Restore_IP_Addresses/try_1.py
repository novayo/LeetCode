class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        '''
        top-down memo
        '''
        
        def recr(index):
            
            if index+1 >= len(s):
                return [[s[index]]]
            
            ret = []
            tmp = recr(index+1)
            for _list in tmp.copy():
                
                if len(_list) < 4:
                    ret.append(_list + [s[index]])
                
                if int(s[index] + _list[-1]) <= 255:
                    _list[-1] = s[index] + _list[-1]
                    ret.append(_list)
            
            return ret
        
        ans = []
        for _list in recr(0):
            if len(_list) == 4 and all(len(x) == 1 or x[0] != '0' for x in _list):
                ans.append('.'.join(_list[::-1]))
        return ans
                