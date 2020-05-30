class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        
        def recr(_list, count=2, index=-1, layer=0):
            nonlocal ans
            
            for i in range(len(_list)-count, index, -1):
                target = ''.join(_list[i:i+count])
                if target == target[::-1]:
                    # print(layer, _list[:i] + [target] + _list[i+count:])
                    # print(target)
                    ans.append(_list[:i] + [target] + _list[i+count:])
                    recr(ans[-1], 2, i, layer+1)
            
            if count < len(s):
                recr(_list, count+1, index, layer)
        
        ans.append(list(s))
        recr(ans[0])
        return ans
