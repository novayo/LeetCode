class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        numA = numB = 0
        _dict = collections.Counter(secret)
        
        for i,v in enumerate(secret):
            if v == guess[i]:
                _dict[v] -= 1
                numA += 1
                
        for i,v in enumerate(guess):
            if v != secret[i]:
                if _dict[v] > 0:
                    numB += 1
                _dict[v] -= 1
                
                
        return str(numA) + "A" + str(numB) + "B"
