class Solution:
    def titleToNumber(self, s: str) -> int:
        return sum([(ord(value)-64) * (26**index) for index, value in enumerate(s[::-1])])
