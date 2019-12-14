class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = S.replace('-', '').upper()
        ans = collections.deque()
        if len(S)%K != 0: ans.append(S[:len(S)%K])
        
        for i in range(len(S)%K, len(S), K):
            ans.append(S[i:i+K])
        return '-'.join(ans)
