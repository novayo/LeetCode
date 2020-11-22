class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        '''
        valid: 紀錄words個數
        maxlen: word最大長度
        backtracking:
            * 每一個就去跑index~index+maxlen，看看這之中有沒有valid的
                * 有的話，found[target] += 1
                * 沒有就繼續找
            * 回傳條件
                * found == valid 回傳True
                * 找太多符合的了，回傳False => found[target] > valid[target]
                * 都沒找到就回傳False
        '''
        ans = []
        valid = collections.defaultdict(int)
        totalLen = 0
        maxlen = 0
        for word in words:
            valid[word] += 1
            maxlen = max(maxlen, len(word))
            totalLen += len(word)
           
        
        # 如果words總長度 > s，回傳False
        if totalLen > len(s):
            return []
        
        
        end = False
        def backtracking(startIndex, found, beginning):
            nonlocal end
            
            if end:
                return True
            
            if (found == valid):
                ans.append(beginning)
                return True
            
            target = ""
            for i in range(0, maxlen):
                if (startIndex + i >= len(s)):
                    end = True
                    return True
                
                target += s[startIndex + i]
                
                if target in valid:
                    if found[target] >= valid[target]:
                        return False
                    
                    found[target] += 1
                    if backtracking(startIndex + i + 1, found, beginning):
                        return True
                    found[target] -= 1
            return False
        
        
        for i in range(len(s)):
            backtracking(i, collections.defaultdict(int), i)
        
        return ans