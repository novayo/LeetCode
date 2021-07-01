class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        
        digits[i] += 1
        carry = 0
        
        while i >= 0:
            digits[i] += carry
            
            if digits[i] >= 10:
                digits[i] -= 10
                carry = 1
                i -= 1
            else:
                carry = 0
                break
        
        if carry:
            digits.insert(0, 1)
        
        return digits
