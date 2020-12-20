class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list = []
        self.curIndex = 0

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.list.append(number)

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        seen = set()
        for v in self.list:
            if value-v in seen:
                return True
            seen.add(v)
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)