class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def recr(start=1, _list=[]):
            if len(_list) == k:
                ans.append(_list)
                return
            
            for i in range(start, n+1):
                recr(i+1, _list + [i])
        
        ans = []
        recr()
        return ans
