class Solution:
    def nthUglyNumber(self, n: int) -> int:
        '''
        用2 3 5由小到大產生乘積
        '''
        arr = [0] * n
        arr[0] = 1
        
        index = [0,0,0]
        power = [2,3,5]
        
        for i in range(1, n):
            arr[i] = min(power)
            
            if arr[i] == power[0]:
                index[0] += 1
                power[0] = arr[index[0]] * 2
            
            if arr[i] == power[1]:
                index[1] += 1
                power[1] = arr[index[1]] * 3
            
            if arr[i] == power[2]:
                index[2] += 1
                power[2] = arr[index[2]] * 5
        
        return arr[-1]
