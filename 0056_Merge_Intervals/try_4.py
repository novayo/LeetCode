class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        binary search
        '''
        arr = []
        
        for start, end in intervals:
            i = bisect.bisect_left(arr, start)
            j = bisect.bisect_right(arr, end)
            
            if i%2 == 0 and j%2 == 0:
                arr[i:j] = [start, end] # 1357 => [0, 8] => return 08
            elif i%2 == 0 and j%2 == 1:
                arr[i:j] = [start]   # 1357 => [0, 2] => return 0357
            elif i%2 == 1 and j%2 == 0:
                arr[i:j] = [end]
            else:
                arr[i:j] = []
        
        ans = []
        for i in range(len(arr)//2):
            ans.append([arr[i*2], arr[i*2+1]])
        return ans