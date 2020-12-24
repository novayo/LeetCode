class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        '''
        不然就是，
        Alice: 如果B[i]很大，則選擇A[i]（因為不讓B[i]選擇）
        Bob: 如果B[i]很大，則選擇B[i]（因為B要選大的）
        '''
        
        sumList = [] # sum, index, AliceValue
        for i in range(len(aliceValues)):
            sumList.append((aliceValues[i] + bobValues[i], i, aliceValues[i]))
        
        sumList.sort()
        
        alice = bob = 0
        for i in range(len(aliceValues)):
            if i%2 == 0:
                alice += aliceValues[sumList[len(aliceValues)-i-1][1]]
            else:
                bob += bobValues[sumList[len(aliceValues)-i-1][1]]
        
        if alice > bob:
            return 1
        elif alice == bob:
            return 0
        else:
            return -1
