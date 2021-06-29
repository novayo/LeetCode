class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ans = cur = cur_one = 0
        ones = collections.deque()
        
        for num in nums:
            if num == 1:
                cur += 1
                cur_one += 1
            else:
                if k > 0:
                    cur += 1
                    if len(ones) >= k:
                        remove = ones.pop()
                        cur -= remove+1
                    ones.appendleft(cur_one)
                    cur_one = 0
                else:
                    if cur > 0:
                        cur -= 1
                
            ans = max(ans, cur)
        
        return ans
