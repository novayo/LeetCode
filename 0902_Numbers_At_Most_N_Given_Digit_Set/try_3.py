class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        try_length = len(digits)
        n_digits_length = 0
        n_list = collections.deque()
        
        # get n_digits
        tmp_n = n
        while tmp_n > 0:
            n_list.appendleft(str(tmp_n % 10))
            n_digits_length += 1
            tmp_n //= 10
        
        
        # calculate number of less than n digits
        ans = 0
        for i in range(1, n_digits_length):
            ans += try_length ** i
        
        
        # calculate number of n digit => use binary search to reduce search time
        considered_index = 0
        while considered_index < n_digits_length:
            target = n_list[considered_index]
            remain_num = bisect.bisect_left(digits, target) # remain num
            
            ans += try_length ** (n_digits_length - (considered_index+1)) * remain_num * 1 # choose target_in_digits and calculate remain
            
            # if search result is not equal to the digits => is lower to target
            if not (remain_num < try_length and target == digits[remain_num]):
                break
            
            if considered_index + 1 == n_digits_length: # if hit all element => 1*1*1*1*... => return 0 => but we have to count in 1
                ans += 1
                
            considered_index += 1
        
        return ans