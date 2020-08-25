class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # binary search
        '''
        偶數個：找到最中間的兩個index相加除二即可
        奇數個：直接找最中間的值
        由於兩個都是排序過的
        所以可以用binary search來尋找
        
        1 
        如果先不用binary search加速
        時間複雜度：O(m+n)
        
        先找出要找的index是哪個或是哪兩個，
        再去找左右兩邊即可
        '''
        
        total_len = len(nums1) + len(nums2)
        target = (total_len) // 2 # 如果total_len%2 == 0，則要再多找一個
        found = []
        count = 0
        i = j = 0
        
        # 直接多找一個
        while count <= target:
            if i < len(nums1) and j < len(nums2):
                if nums1[i] < nums2[j]:
                    found.append(nums1[i])
                    i += 1
                else:
                    found.append(nums2[j])
                    j += 1
            elif i < len(nums1):
                found.append(nums1[i])
                i += 1
            else:
                found.append(nums2[j])
                j += 1
            
            count += 1
        
        if total_len % 2 == 0:
            return (found[-1]+found[-2]) / 2
        else:
            return found[-1]
