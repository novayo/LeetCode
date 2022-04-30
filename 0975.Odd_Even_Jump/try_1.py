from sortedcontainers import SortedList

class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        n = len(arr)
        smaller = SortedList()
        bigger = SortedList()
        
        odd = [False] * n
        even = [False] * n
        
        # odd
        odd[-1] = even[-1] = True
        for i in range(n-1, -1, -1):
            # bigger
            idx = bigger.bisect_left((arr[i],))
            if idx < len(bigger):
                odd[i] = even[bigger[idx][1]]
            bigger.add((arr[i], i))
            
            # smaller
            idx = smaller.bisect_left((-arr[i],))
            if idx < len(smaller):
                even[i] = odd[smaller[idx][1]]
            smaller.add((-arr[i], i))
        
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
