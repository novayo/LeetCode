class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        先計算每個key的個數
        之後用quick-select依照個數挑選 k largest即可 => 其key代表frequency
        '''
        
        counter = collections.Counter(nums)
        
        # 計算個數 => O(n)
        number_nums = []
        for key, value in counter.items():
            number_nums.append((value, key))
        
        
        # 針對第一個element做quick select => O(n)
        def quick_select(nums, k):
            
            # 選擇pivot
            pivot = random.randint(0, len(nums)-1)
            nums[pivot], nums[-1] = nums[-1], nums[pivot]
            
            # 先整理小於的到前面
            i = j = 0
            while j < len(nums) - 1:
                if nums[j][0] < nums[-1][0]:
                    nums[j], nums[i] = nums[i], nums[j]
                    i += 1
                j += 1
            
            nums[i], nums[-1] = nums[-1], nums[i]
            
            # 決定範圍
            l = len(nums) - i
            if l > k:
                return quick_select(nums[i:], k)
            elif l == k:
                return nums[i:]
            else:
                return quick_select(nums[:i], k - l) + nums[i:]
                
        ret = quick_select(number_nums, k)
        
        # get answer => O(n)
        ans = [0] * k
        for i in range(k):
            ans[i] = ret[i][1]
        return ans
