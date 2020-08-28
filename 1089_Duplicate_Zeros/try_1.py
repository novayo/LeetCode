class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        '''
        先算總共有幾個0（count）
        
        之後從右邊看回來，
        如果是0，先讓count -= 1
        
        遇到的每個值，如果當下的index+count < len(arr)，就讓此值移到index+count
        如果是0，就把index+count+1改成0
        '''
        
        # 找幾個0
        count = 0
        for value in arr:
            if value == 0:
                count += 1
        
        for index in range(len(arr)-1, -1, -1):
            if arr[index] == 0:
                count -= 1
            
            if index + count < len(arr):
                arr[index+count] = arr[index]
            
            if arr[index] == 0 and index+count+1 < len(arr):
                arr[index+count+1] = 0
                
