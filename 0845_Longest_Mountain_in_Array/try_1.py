class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        ans = i = 0
        
        while i < len(arr)-1:
            if arr[i] < arr[i+1]:
                j = i+1
                asc = True
                while j < len(arr)-1:
                    if asc:
                        if arr[j] > arr[j+1]:
                            asc = False
                        elif arr[j] == arr[j+1]:
                            break
                    else:
                        if arr[j] <= arr[j+1]:
                            break
                    j += 1
                
                if asc == False:
                    ans = max(ans, j-i+1)
                i = j
            else:
                i += 1
        
        return ans
