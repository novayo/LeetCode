class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        all_x = set()
        for s, e in firstList + secondList:
            all_x.add(s)
            all_x.add(e)
        
        ans = []
        pre = -1
        inA = inB = False
        aIdx = bIdx = cur = 0
        for x in sorted(all_x):
            if aIdx >= len(firstList) or bIdx >= len(secondList):
                break
            
            if x == firstList[aIdx][0] and x == secondList[bIdx][1]:
                ans.append([x,x])
                inA, inB = True, False
                bIdx += 1
                continue
            elif x == firstList[aIdx][1] and x == secondList[bIdx][0]:
                ans.append([x,x])
                inA, inB = False, True
                aIdx += 1
                continue
            
            if x == firstList[aIdx][0]:
                inA = True
            if x == firstList[aIdx][1]:
                inA = False
                aIdx += 1
            if x == secondList[bIdx][0]:
                inB = True
            if x == secondList[bIdx][1]:
                inB = False
                bIdx += 1
            
            if inA is True and inB is True:
                pre = x
            elif pre != -1:
                ans.append([pre, x])
                pre = -1
        return ans