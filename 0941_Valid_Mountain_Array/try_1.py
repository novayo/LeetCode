class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        # loop
        '''
        直接掃過去，看是否是遞增或遞減
        '''
        if len(A) < 3:
            return False
        
        if A[0] >= A[1]:
            return False
        
        went_peak = False
        
        for i in range(len(A)-1):
            if went_peak:
                if A[i] <= A[i+1]:
                    return False
            else:
                if A[i] > A[i+1]:
                    went_peak = True
                elif A[i] == A[i+1]:
                    return False
                
        return True if went_peak else False
