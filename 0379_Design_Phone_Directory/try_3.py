class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.avaliable = set()
        self.used = set()
        self.maxNumbers = maxNumbers

    def get(self) -> int:
        ret = -1
        
        if self.avaliable:
            ret = self.avaliable.pop()
        elif len(self.used) < self.maxNumbers:
            ret = len(self.used)
        
        self.used.add(ret)
        return ret

    def check(self, number: int) -> bool:
        return number not in self.used

    def release(self, number: int) -> None:
        if number in self.used:
            self.used.remove(number)
            self.avaliable.add(number)


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)
