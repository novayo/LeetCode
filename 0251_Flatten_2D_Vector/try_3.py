class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.flatten_arr = self._build(vec)
        self.index = 0

    def _build(self, vec):
        # iterate => preorder
        ans = []
        stack = [(vec, 0)]
        while stack:
            _v, ind = stack.pop()
            
            if ind >= len(_v):
                continue
            else:
                stack.append((_v, ind+1))
                
            if isinstance(_v[ind], list):
                stack.append((_v[ind], 0))
            else:
                ans.append(_v[ind])
        return ans
        
    def next(self) -> int:
        self.index += 1
        return self.flatten_arr[self.index-1]

    def hasNext(self) -> bool:
        return self.index < len(self.flatten_arr)


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()
