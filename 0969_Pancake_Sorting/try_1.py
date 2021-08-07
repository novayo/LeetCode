class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []
        for a in range(len(arr), 1, -1):
            index = arr.index(a)
            ans.append(index+1)
            ans.append(a)
            arr[:index+1] = arr[:index+1][::-1]
            arr[:a] = arr[:a][::-1]
        return ans 
