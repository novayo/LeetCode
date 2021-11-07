class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
        s = set()
        s.add(2)
        s.add(1)
        s.add(2)    hash function(2) => 數學運算
        
        # s => set(1,2)
        search => 3 in s => O(1)
        
        '''
        # nums1 => set
        nums1_set = set()
        for num1 in nums1:
            nums1_set.add(num1)
        
        # nums2 => set
        nums2_set = set()
        for num2 in nums2:
            nums2_set.add(num2)
        
        
        ans = []
        for num1 in nums1_set:
            if num1 in nums2_set:
                ans.append(num1)
        
        return ans
        
#         # nums2 => set => O(n)
#         nums2_set = set()
#         for num2 in nums2:
#             nums2_set.add(num2)
        
#         # loop nums1 => check if the element in nums1 locates in nums2 as well or not.
#         ans = set() # 去除重複
        
#         # O(n)
#         for num1 in nums1:
#             if num1 in nums2_set: # O(1)
#                 ans.add(num1)
        
#         return list(ans)