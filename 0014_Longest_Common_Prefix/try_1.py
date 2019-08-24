class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == []:
            return ""
        minStr = min(strs, key=len)
        del strs[strs.index(minStr)]
        for i in range(len(minStr)):
            for j in range(len(strs)):
                if minStr[i] != strs[j][i]:
                    return minStr[0:i]
        return minStr
