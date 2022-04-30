class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        n = len(arr)
        
        bigger = [-1] * n
        stack = []
        for val, idx in sorted((arr[i], i) for i in range(n)):
            while stack and stack[-1] < idx:
                bigger[stack.pop()] = idx
            stack.append(idx)
        
        smaller = [-1] * n
        stack = []
        for val, idx in sorted((-arr[i], i) for i in range(n)):
            while stack and stack[-1] < idx:
                smaller[stack.pop()] = idx
            stack.append(idx)
            
        odd = [False] * n
        even = [False] * n
        
        # odd
        odd[-1] = even[-1] = True
        for i in range(n-1, -1, -1):
            # bigger
            idx = bigger[i]
            if idx >= 0:
                odd[i] = even[idx]
            
            # smaller
            idx = smaller[i]
            if idx >= 0:
                even[i] = odd[idx]
        
        return sum(odd)
        
'''
奇數 => 找下一個略大於等於
偶數 => 找下一個略小於等於

1. 做出兩種的關係 O(nlogn) using bst
2. 

O(n) => 
dp =         [ [F, F]   [F, F]   [T,F]   [F,F]   [T,T] ]
               x  x  x  O  O
Input: arr = [10,13,12,14,15]
Output: 2
'''
