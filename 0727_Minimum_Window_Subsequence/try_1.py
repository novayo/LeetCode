class Solution:
    def minWindow(self, S: str, T: str) -> str:
        s = t = 0
        slen = len(S)
        start = -1
        
        while s < len(S):
            if S[s] == T[t]:
                t += 1
                if t == len(T):
                    end = s + 1
                    
                    while True:
                        t -= 1
                        if t < 0: break
                            
                        while True:
                            if S[s] == T[t]:
                                s -= 1
                                break
                            s -= 1
                    
                    s += 1
                    t += 1
                    
                    if end - s < slen:
                        slen = end - s
                        start = s
            s += 1
            
        return "" if start == -1 else S[start: start+slen]
