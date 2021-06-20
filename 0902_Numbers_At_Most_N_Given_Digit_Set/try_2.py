class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        try_length = len(digits)
        n_digits_length = 0
        digits_list = collections.deque()
        
        # get n_digits
        tmp_n = n
        while tmp_n > 0:
            digits_list.appendleft(str(tmp_n % 10))
            n_digits_length += 1
            tmp_n //= 10
        
        
        # calculate number of less than n digits
        ans = 0
        for i in range(1, n_digits_length):
            ans += try_length ** i
        
        
        # calculate number of n digit => use binary search to reduce search time
        considered_index = 0
        while considered_index < n_digits_length:
            target = digits_list[considered_index]
            remain_num = bisect.bisect_left(digits, target) # remain num
            
            ans += try_length ** (n_digits_length - (considered_index+1)) * remain_num * 1 # choose target_in_digits and calculate remain
            
            if remain_num >= try_length: # if target is higher than else => take all
                break
            elif target == digits[remain_num]:
                if considered_index + 1 == n_digits_length: # if hit all element => 1*1*1*1*... => return 0 => but we have to count in 1
                    ans += 1
                considered_index += 1
            else:
                break
        
        return ans