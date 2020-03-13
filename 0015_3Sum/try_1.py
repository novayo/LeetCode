class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        ret = set()
        negtiveList = []
        zeroList = []
        positiveList = []
        for n in nums:
            if n < 0:
                negtiveList.append(n)
            elif n == 0:
                zeroList.append(n)
            else:
                positiveList.append(n)
        
        negtiveSet = set(negtiveList)
        positiveSet = set(positiveList)
        ### four condition
        # 0 0 0
        if len(zeroList) >= 3:
            ret.add((0,0,0))
        
        # - 0 +  =>  abs(-) = +
        if len(zeroList) > 0:
            for n in negtiveList:
                tmp = abs(n)
                if tmp in positiveSet:
                    ret.add((n, 0, tmp))
        
        # - - +
        for i in range(len(negtiveList)):
            for j in range(i+1, len(negtiveList)):
                if i == j: continue
                tmp = abs(negtiveList[i] + negtiveList[j])
                if tmp in positiveSet:
                    ret.add((negtiveList[i], negtiveList[j], tmp))
        
        # - + +
        for i in range(len(positiveList)):
            for j in range(i+1, len(positiveList)):
                if i == j: continue
                tmp = -1 * (positiveList[i] + positiveList[j])
                if tmp in negtiveSet:
                    ret.add((tmp, positiveList[i], positiveList[j]))
        
        return list(ret)
