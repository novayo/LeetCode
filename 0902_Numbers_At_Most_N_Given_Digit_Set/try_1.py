class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        try_length = len(digits)
        n_digits_length = 0
        digits_list = collections.deque()
        
        # get n_digits
        tmp_n = n
        while tmp_n > 0:
            digits_list.appendleft(tmp_n % 10)
            n_digitsa_length += 1
            tmp_n //= 10
        
        
        # calculate number of less than n digits
        ans = 0
        for i in range(1, n_digits_length):
            ans += try_length ** i
        
        
        # calculate number of n digit
        def recr(startIndex: int, level: int):
            if startIndex >= n_digits_length:
                return 1
            
            ret = 0
            for index, digit in enumerate(digits):
                digit = int(digit)
                if digit > digits_list[startIndex]: # because digits is sorted in non-decreasing order, we dont need to care the rest
                    break
                elif digit == digits_list[startIndex]:
                    ret += recr(startIndex + 1, level + 1)
                else:
                    remain = n_digits_length - (level+1) # calculate rest digits
                    ret += try_length ** remain      # we can choose any rest digits
                    
            return ret
        
        ans += recr(0, 0)
        return ans
  