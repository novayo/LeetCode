class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = []
        
        for i in range(1, n+1):
            index = arr[:n-i+1].index(i)
            
            ans.append(index+1)
            arr[:index+1] = arr[:index+1][::-1]
            ans.append(n-i+1)
            arr[:n-i+1] = arr[:n-i+1][::-1]

        ans.append(n)
        return ans