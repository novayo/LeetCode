class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits:
            return [1]
        
        digits[-1] += 1
        
        count = 0
        for i in range(len(digits)):
            digits[~i] += count
            
            if digits[~i] == 10:
                digits[~i] = 0
                count = 1
            else:
                break
                
        return digits if digits[0] != 0 else [1] + digits
