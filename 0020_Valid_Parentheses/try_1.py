class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        buffer = []
        for i in s:
            if (i == ')'):
                if (len(buffer) > 0 and buffer[-1] == '('):
                    buffer.pop()
                else:
                    return False
            elif (len(buffer) > 0 and i == ']'):
                if (buffer[-1] == '['):
                    buffer.pop()
                else:
                    return False
            elif (len(buffer) > 0 and i == '}'):
                if (buffer[-1] == '{'):
                    buffer.pop()
                else:
                    return False
            else:
                buffer.append(i)
        if (len(buffer) == 0):
            return True
        else:
            return False
