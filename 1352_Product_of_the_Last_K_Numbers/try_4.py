class ProductOfNumbers:

    def __init__(self):
        self.last_zero = float('inf')
        self.premuti = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.last_zero = 1
            self.premuti.append(1)
        else:
            self.last_zero += 1
            self.premuti.append(self.premuti[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= self.last_zero:
            return 0
        return self.premuti[-1] // self.premuti[-k-1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
