class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # binary search
        '''
        先抓出一個，之後用binary search去找target-numbers在哪即可
        分成兩邊，
        如果target-numbers > numbers，就找右邊
        反之找左邊
        
        時間複雜度：O(nlogn)
        空間複雜度：O(1)
        '''
        
        for i in range(len(numbers)):
            find_target = target - numbers[i]
            
            # binary search
            left = right = -1
            
            if find_target >= numbers[i]:
                left, right = i+1, len(numbers)-1
            else:
                left, right = 0, i
            
            while left < right:
                mid = left + (right - left) // 2
                if numbers[mid] > find_target:
                    right = mid
                elif numbers[mid] == find_target:
                    return sorted([i+1, mid+1])
                else:
                    left = mid + 1
                    
                    
