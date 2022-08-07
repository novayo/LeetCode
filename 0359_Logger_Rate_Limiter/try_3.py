class Logger:

    def __init__(self):
        self.cache = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.cache and self.cache[message] + 10 > timestamp:
            return False
        self.cache[message] = timestamp
        return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
