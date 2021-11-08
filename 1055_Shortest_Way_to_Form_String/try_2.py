class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        target_processed = self.Preprocess(source, target)
        if target_processed == -1:
            return -1

        ans, pre = 1, -1
        for i in target_processed:
            if i <= pre:
                ans += 1
            pre = i
        return ans
    
    def Preprocess(self, source, target):
        s = set(source)
            
        target_index = []
        i=0
        for t in target:
            if t not in s:
                return -1

            while t != source[i]:
                i+=1
                if i >= len(source):
                    i = 0
            target_index.append(i)
            i += 1
            if i >= len(source):
                i = 0
        return target_index