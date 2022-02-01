class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        ans = []
        
        def recr(start):
            nonlocal ans
            
            hrs = (arr[0]*10+arr[1])
            mins = (arr[2]*10+arr[3])
            
            if (0 <= hrs <= 23 and 0 <= mins <= 59):
                if not ans or (hrs*60+mins > ans[0]*60+ans[1]):
                    ans = [hrs, mins]
            
            for i in range(start, 4):
                arr[start], arr[i] = arr[i], arr[start]
                recr(start+1)
                arr[start], arr[i] = arr[i], arr[start]
        
        recr(0)
        if not ans:
            return ''
        else:
            return str(ans[0]).zfill(2) + ':' + str(ans[1]).zfill(2)
