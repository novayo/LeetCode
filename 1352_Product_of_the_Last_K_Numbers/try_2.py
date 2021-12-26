class ProductOfNumbers:

    def __init__(self):
        self.preProd = [1]
        self.valid_k = 0

    def add(self, num: int) -> None:
        if self.preProd[-1] == 0:
            self.preProd.append(num)
        else:
            self.preProd.append(num * self.preProd[-1])
        
        if num == 0:
            self.valid_k = 0
        else:
            self.valid_k += 1

    def getProduct(self, k: int) -> int:
        start = len(self.preProd)-k-1
        
        if k > self.valid_k:
            return 0
        
        return self.preProd[-1] // max(self.preProd[start], 1)


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
