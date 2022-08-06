class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        # O(nlogn) time / O(n) space - where n is the length of the input arr
        n = len(arr)
        i_arr = [[v, i] for i, v in enumerate(arr)]
        
        # get bigger
        bigger = {}
        dec_stack = []
        for _, idx in sorted(i_arr):
            while dec_stack and idx >= dec_stack[-1]:
                bigger[dec_stack.pop()] = idx
            dec_stack.append(idx)
        
        # get smaller
        smaller = {}
        dec_stack = []
        for _, idx in sorted(i_arr, key=lambda x: (-x[0], x[1])):
            while dec_stack and idx >= dec_stack[-1]:
                smaller[dec_stack.pop()] = idx
            dec_stack.append(idx)
        
        # dp
        odd_dp = [False] * n
        even_dp = [False] * n
        odd_dp[-1] = even_dp[-1] = True
        
        for i in range(n-2, -1, -1):
            # odd
            if i in bigger:
                odd_dp[i] = even_dp[bigger[i]]
            
            # even
            if i > 0 and i in smaller:
                even_dp[i] = odd_dp[smaller[i]]
        
        return sum(odd_dp)