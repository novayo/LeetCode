class Vector2D:
    '''
    用這兩個變數來指向對應的index，
    如此一來可以減少建立list的時間，也可以節省記憶體
    '''
    def __init__(self, v: List[List[int]]):
        self.v = v
        self.inner = 0
        self.outer = 0

    def go_to_next_outer(self):
        # 如果inner滿了，就走到下一個outer
        # 否則不動
        # 避免 [[1], [], [], [3,4]]的情況才用while
        while self.outer < len(self.v) and self.inner == len(self.v[self.outer]):
            self.outer += 1
            self.inner = 0
    
    def next(self) -> int:
        self.go_to_next_outer()
        tmp = self.v[self.outer][self.inner]
        self.inner += 1
        return tmp

    def hasNext(self) -> bool:
        # 直接看看是否inner已經到底了，如果到底就往下走一格，
        # 反正這裡不走，第20行也會走一次
        self.go_to_next_outer()
        
        # 再去看看是否outer有沒有小於總長度就好
        return self.outer < len(self.v)


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()
