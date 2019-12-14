"""
The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""
class Solution:
    def __init__(self):
        self.tmp = collections.deque()
        self.not_done = True
        
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        while (self.not_done):
            a = read4(buf)
            if a != 0:
                for i in range(a):
                    self.tmp.append(buf[i])
            else:
                self.not_done = False
                for i in range(0, len(buf)):
                    buf[i] = ' '
                    if (buf[i+1] == ' '): break
                break
                
        for i in range(n):
            buf[i] = '' if len(self.tmp) == 0 else self.tmp.popleft()
                
        return n

