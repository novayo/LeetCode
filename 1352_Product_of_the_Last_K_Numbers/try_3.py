'''

[1,2,3,4,5,6,7]
prefix_mul => [1, 1*2, 1*2*3, ... 1*2*3*4*5*6*7]

[1,2,3,0,5,6,7]
prefix_mul => [1, 1*2, 1*2*3, 0, 5, 5*6, 5*6*7]
lastest_0_k = 4

init:
    lastest_0_k = float('inf')
    current_mul = 1
    prefix_mul = []

# O(1) time
add(num)
    if num == 0:
        lastest_0_k = 1
        current_mul = 1
        prefix_mul.append(num)
        return
    
    current_mul *= num
    prefix_mul.append(current_mul)
    lastest_0_k += 1

# O(1) time
getProduct(k)
    if k >= lastest_0_k:
        return 0
    return prefix_mul[-1] // prefix_mul[-1-k]
'''

class ProductOfNumbers:

    def __init__(self):
        self.lastest_0_k = float('inf')
        self.current_mul = 1
        self.prefix_mul = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.lastest_0_k = 1
            self.current_mul = 1
        else:        
            self.current_mul *= num
            self.lastest_0_k += 1
            
        self.prefix_mul.append(self.current_mul)
        
    def getProduct(self, k: int) -> int:
        if k >= self.lastest_0_k:
            return 0
        return self.prefix_mul[-1] // self.prefix_mul[-1-k]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
