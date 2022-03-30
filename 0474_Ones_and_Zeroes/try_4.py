class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        def recr(index):
            if index >= len(strs):
                return {(0, 0, 0)}
            
            counter = collections.Counter(strs[index])
            
            ret = recr(index+1)
            for length, zero, one in ret.copy():
                zero += counter['0']
                one += counter['1']
                if zero <= m and one <= n:
                    ret.add((length+1, zero, one))
            return ret
        
        return max(recr(0), key=lambda x: x[0])[0]
        