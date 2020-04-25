class Solution:
    def jump(self, nums: List[int]) -> int:
        # 從尾巴開始往前
        # 去看說 現在的這個位置 有哪些可以到
        # 再去看看那些位置 又有哪些可以到，先到0，就直接回傳找的次數
        
        tmp = collections.Counter(nums)
        if len(tmp) == 1:
            return len(nums)-1
        
        queue = collections.deque()
        queue.appendleft((len(nums)-1, 1))
        
        while queue:
            index, times = queue.popleft()
            target = index
            while index >= 0:
                index -= 1
                if index + nums[index] >= target:
                    if index == 0:
                        return times
                    queue.appendleft((index, times+1))
        return 0
