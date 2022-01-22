class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        '''
        記得 最左邊的0的index => 一但有k+1個出現了，則把最左邊的拿掉，index往後移到下一個0
        走的過程中紀錄最大值
        '''
        ans = cur_k = i = j = offset = 0
        index = collections.deque()
                
        while j < len(nums):
            if nums[j] == 0:
                index.append(j)
                if cur_k < k:
                    cur_k += 1
                elif k > 0:
                    _i = index.popleft()
                    i = index[0] # 若k=0, index皆為空，會有問題
                    offset = i-_i-1 # ...0 1 1 0 ... => 更新到右邊的0的時候，左邊的兩個2也要算進去答案
                else:
                    i = j+1
            
            j += 1
            ans = max(ans, j-i+offset)
        return ans
