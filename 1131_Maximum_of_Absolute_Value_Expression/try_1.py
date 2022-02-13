class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        '''
2 <= len <= 40000
+-10**6
Input: arr1 = [1,2,3,4], arr2 = [-1,4,5,6]
Output: 13

return max of |arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i - j|
brute force: O(n^2)

=> time comp.: O(n)
=> space comp.: O(n) => O(1)
dp1 => i + arr1[i] + arr2[i] => [x,x,x,x,x,x,x]
dp2 => i + arr1[i] - arr2[i] => [y,y,y,y,y,y,y]
dp3 => i + -arr1[i] + arr2[i]
dp4 => i + -arr1[i] - arr2[i]



arr1 2[i] => arr1 2[j]
    (arr1[i] + arr2[i]) - (arr1[j] + arr2[j]) => dp1[i] - dp1[j] => max
arr1 2[i] < arr1 2[j]
    - (arr1[i] + arr2[i]) + (arr1[j] + arr2[j]) => dp4[i] - dp4[j] => max
arr1[i] > arr1[j] and arr2[i] < arr2[j]
    (arr1[i] - arr2[i]) - (arr1[j] - arr2[j]) => dp2[i] - dp2[j] => max
arr1[i] < arr1[j] and arr2[i] > arr2[j]
    -arr1[i] + arr2[i] + (arr1[j] - arr2[j]) => dp3[i] - dp3[j] => max
        '''
        n = len(arr1)
        ans = -float('inf')
        
        coeff = [(1,1), (1,-1), (-1,1), (-1,-1)]
        for i, (p, q) in enumerate(coeff):
            cur_min = float('inf')
            cur_max = -float('inf')
            for i, (a1, a2) in enumerate(zip(arr1, arr2)):
                sum = i + a1*p + a2*q
                cur_min = min(cur_min, sum)
                cur_max = max(cur_max, sum)
            ans = max(ans, cur_max - cur_min)
        return ans
            
            
            
            
            
            
            