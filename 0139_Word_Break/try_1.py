class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        tmp = s
        for i in wordDict:
            if s == "": break
            s = ' '.join(map(str, s.split(i)))
        if ''.join(map(str, s.split(' '))) == "":
            return True
        
        s = tmp
        for i in sorted(wordDict, key=len):
            if s == "": break
            s = ' '.join(map(str, s.split(i)))
        if ''.join(map(str, s.split(' '))) == "":
            return True
        
        s = tmp
        for i in sorted(wordDict):
            if s == "": break
            s = ' '.join(map(str, s.split(i)))
        if ''.join(map(str, s.split(' '))) == "":
            return True
        
        s = tmp
        for i in sorted(wordDict, key=len)[::-1]:
            if s == "": break
            s = ' '.join(map(str, s.split(i)))
        if ''.join(map(str, s.split(' '))) == "":
            return True
        else:
            return False
