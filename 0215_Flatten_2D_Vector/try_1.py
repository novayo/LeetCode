class Vector2D:
    '''
    直接用一個list存起來並用一個index去只向它
    但這個方法會用到額外的記憶體 以及 會去跑額外的時間（建立list時）
    因此這方法不好
    '''
    def __init__(self, v: List[List[int]]):
        self.index = -1
        self.v = []
        for row in v:
            self.v += row

    def next(self) -> int:
        self.index += 1
        return self.v[self.index]

    def hasNext(self) -> bool:
        return self.index + 1 < len(self.v)


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()
