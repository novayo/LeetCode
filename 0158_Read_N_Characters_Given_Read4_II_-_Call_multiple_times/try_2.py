# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    def __init__(self):
        self.rest = []
        
    def read(self, buf: List[str], n: int) -> int:
        while len(self.rest) < n:
            tmp = [''] * 4
            num = read4(tmp)
            if num == 0:
                break
            self.rest.extend(tmp[:num])
        
        if len(self.rest) < n:
            n = len(self.rest)
        buf[:n] = self.rest[:n]
        self.rest = self.rest[n:]
        return n

