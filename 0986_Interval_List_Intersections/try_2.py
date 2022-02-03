class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        '''
        sweep line
        '''
        flat1 = []
        for tmp in firstList:
            flat1 += tmp
        
        flat2 = []
        for tmp in secondList:
            flat2 += tmp
        
        ans = []
        count = i = j = 0
        while i < len(flat1) and j < len(flat2):
            # choose lower
            lower, is_start = 0, False
            if flat1[i] < flat2[j]:
                lower = flat1[i]
                is_start = i%2 == 0
                i += 1
            elif flat1[i] > flat2[j]:
                lower = flat2[j]
                is_start = j%2 == 0
                j += 1
            else:
                if i%2 != j%2:
                    ans.append(flat1[i])
                    ans.append(flat1[i])
                    count = 1
                    i += 1
                    j += 1
                    continue
                else:
                    lower = flat1[i]
                    is_start = i%2 == 0
                    i += 1
            
            if is_start:
                count += 1
                if count == 2:
                    ans.append(lower)
            else:
                if count == 2:
                    ans.append(lower)
                count -= 1
           
        ret = []
        for i in range(len(ans) // 2):
            ret.append(ans[i*2:i*2+2])
        return ret
                
