class Solution:
    def maxProduct(self, words: List[str]) -> int:
        d = {"a": 2**0, "b": 2**1, "c": 2**2, "d": 2**3, "e": 2**4, "f": 2**5, "g": 2**6,
             "h": 2**7, "i": 2**8, "j": 2**9, "k": 2**10, "l": 2**11, "m": 2**12, "n": 2**13,
             "o": 2**14, "p": 2**15, "q": 2**16, "r": 2**17, "s": 2**18, "t": 2**19, "u": 2**20,
             "v": 2**21, "w": 2**22, "x": 2**23, "y": 2**24, "z": 2**25}
        
        length = []
        for i, word in enumerate(words):
            length.append(len(word))
            n = 0
            tmp = set()
            for w in word:
                if w not in tmp:
                    tmp.add(w)
                    n += d[w]
            words[i] = n
        
        ans = 0
        for i in range(len(words)-1):
            for j in range(i+1, len(words)):
                if words[i] & words[j] == 0:
                    ans = max(ans, length[i]*length[j])
        return ans
