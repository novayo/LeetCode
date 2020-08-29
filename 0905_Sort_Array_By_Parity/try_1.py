class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        # two pointer
        '''
        如果left % 2 == 1 and right % 2 == 0，swap，left += 1，right -= 1
        如果left % 2 == 1 and right % 2 == 1，right -= 1
        如果left % 2 == 0 and right % 2 == 1，pass
        如果left % 2 == 0 and right % 2 == 0，left += 1
        如果left >= right，break
        '''
        
        left = 0
        right = len(A)-1
        while left < right:
            l = A[left]%2
            r = A[right]%2
            
            if l == r == 0:
                left += 1
            elif l == r == 1:
                right -= 1
            elif l == 1 and r == 0:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1
            else:
                left += 1
                right -= 1
        return A
