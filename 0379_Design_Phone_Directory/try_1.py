class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.maxNumbers = maxNumbers
        self.avaliable = set(range(maxNumbers))

    def get(self) -> int:
        if len(self.avaliable) == 0:
            return -1
        else:
            return self.avaliable.pop()

    def check(self, number: int) -> bool:
        return number in self.avaliable

    def release(self, number: int) -> None:
        self.avaliable.add(number)


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)
