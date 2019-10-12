class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        numA = numB = 0
        _dict = collections.defaultdict(int)
        
        for i,v in enumerate(secret):
            if v == guess[i]:
                numA += 1
            else:
                _dict[v] += 1
        
        for i,v in enumerate(guess):
            if v != secret[i] and _dict[v] > 0:
                _dict[v] -= 1
                numB += 1
                
        return str(numA) + "A" + str(numB) + "B"
