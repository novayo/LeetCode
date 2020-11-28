class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        '''
        sliding window:
            * 一個left去記錄左邊的index，而index+字母長度則為現在找的起始word
            * 要去sliding window 一個 word
            * 只要去找for i in range(0, wordLen)即可，因為找一個word，所以後面的倍數index會重複找
        '''
        
        valid = collections.defaultdict(int)
        wordLen = len(words[0])
        totalLen = 0
        
        for word in words:
            valid[word] += 1
            totalLen += len(word)
        
        
        if len(s) < totalLen:
            return []
        
        ans = []
        for i in range(0, wordLen):
            left = i
            find = collections.defaultdict(int)
            
            for j in range(i, len(s)-wordLen+1, wordLen):
                curStr = s[j:j+wordLen]
                if curStr in valid:
                    find[curStr] += 1
                    
                    while find[curStr] > valid[curStr]:
                        find[s[left:left+wordLen]] -= 1
                        left += wordLen
                    
                    if find == valid:
                        ans.append(left)
                else:
                    find = collections.defaultdict(int)
                    left = j + wordLen
        return ans
