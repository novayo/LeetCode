class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # binary search
        '''
        偶數個：找到最中間的兩個index相加除二即可
        奇數個：直接找最中間的值
        
        https://www.youtube.com/watch?v=LPFhl65R7ww
        
        x : x1, x2 | x3, x4, x5, x6
        y : y1, y2, y3, y4, y5 | y6, y7
        
        這裡的binary search比較特別
        主要就是
        
        去猜中間在哪裏，但原本是一個遞增的陣列，
        中間的左邊是由x1,x2,y1~y5去組成的
        中間的右邊是由x3~x6, y6,y7組成的
        
        所以 最中間的值，才有這個特性
        x2 <= y6 and y5 <= x3
        
        而如果x的猜第i個是最中間，
        則y的最中間會在 (len(x)+len(y)+1) // 2 - i
        要用比較少的為基準下去切才不會有長度上的問題
        
        
        而答案會在 奇數個：max(x2, y5) 偶數個：avg(max(x2, y5)+min(x3, y6))
        
        如果 x2 > y6，表示切太多格了（太右邊了），則往左邊走 right = mid
        反之 left = mid + 1
        '''
        
        m, n = len(nums1), len(nums2)
        
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
        
        left_nums1, right_nums1 = 0, m
        while left_nums1 <= right_nums1:
            mid_nums1 = left_nums1 + (right_nums1 - left_nums1) // 2
            mid_nums2 = (m+n+1) // 2 - mid_nums1
            
            if mid_nums1 > 0 and nums1[mid_nums1-1] > nums2[mid_nums2]:
                right_nums1 = mid_nums1 - 1
            elif mid_nums1 < m and nums1[mid_nums1] < nums2[mid_nums2-1]:
                left_nums1 = mid_nums1 + 1
            else:
                if mid_nums1 == 0:
                    ans = nums2[mid_nums2-1]
                elif mid_nums2 == 0:
                    ans = nums1[mid_nums1-1]
                else:
                    ans = max(nums1[mid_nums1-1], nums2[mid_nums2-1])
                
                if (m+n) % 2 == 1:
                    return ans
                
                if mid_nums1 == m:
                    ans += nums2[mid_nums2]
                elif mid_nums2 == n:
                    ans += nums1[mid_nums1]
                else:
                    ans += min(nums1[mid_nums1], nums2[mid_nums2])
                
                return ans / 2
