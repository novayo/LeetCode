class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge_sort(i, j):
            if i > j:
                return []
            elif i == j:
                return [nums[i]]
            
            mid = i + (j - i) // 2
            left = merge_sort(i, mid)
            right = merge_sort(mid+1, j)
            
            ret_array = []
            k1 = k2 = 0
            while k1 < len(left) and k2 < len(right):
                if left[k1] <= right[k2]:
                    ret_array.append(left[k1])
                    k1 += 1
                else:
                    ret_array.append(right[k2])
                    k2 += 1
            
            while k1 < len(left):
                ret_array.append(left[k1])
                k1 += 1
            
            while k2 < len(right):
                ret_array.append(right[k2])
                k2 += 1
            
            return ret_array
        
        return merge_sort(0, len(nums)-1)
        