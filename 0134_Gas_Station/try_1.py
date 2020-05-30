class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = []
        for i in range(len(gas)):
            diff.append(gas[i]-cost[i])  
        
        for i in range(len(gas)):
            if diff[i] >= 0:
                tmp = diff[i]
                for j in range(i+1, i+len(gas)):
                    tmp += diff[j%len(gas)]
                    if tmp < 0:
                        break
                if tmp >= 0:
                    return i
        return -1
