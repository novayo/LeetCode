class ProductOfNumbers:

    def __init__(self):
        self.preProd = [1]
        self.zeros = []

    def add(self, num: int) -> None:
        if self.preProd[-1] == 0:
            self.preProd.append(num)
        else:
            self.preProd.append(num * self.preProd[-1])
        
        if num == 0:
            self.zeros.append(len(self.preProd)-2)

    def getProduct(self, k: int) -> int:
        start = len(self.preProd)-k-1
        
        if len(self.zeros) > 0:
            index_left = bisect.bisect_left(self.zeros, start)
            if index_left != len(self.zeros):
                return 0
        
        return self.preProd[-1] // max(self.preProd[start], 1)


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
