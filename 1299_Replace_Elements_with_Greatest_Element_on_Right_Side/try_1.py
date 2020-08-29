class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # one pass
        '''
        從後面掃過來，初始值為-1
        如果遇到比較小的，直接更換為目前最大值
        如果遇到比較大的，則先更換為目前最大值後，再更新最大值
        '''
        
        max = -1
        for i in range(len(arr)-1, -1, -1):
            if arr[i] <= max:
                arr[i] = max
            else:
                arr[i], max = max, arr[i]
        return arr
