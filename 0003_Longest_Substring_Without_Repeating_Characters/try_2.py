class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tmpString, maxLength, length = "", 0, 0
        for val in s:
            if val in tmpString:
                tmpString = tmpString[tmpString.index(val)+1::]
            tmpString += val
            length = len(tmpString)
            if (length > maxLength):
                maxLength = length
        return maxLength
