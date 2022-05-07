class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        def comb(cards, idx, cur, left, right, length):
            if len(cur) == length:
                left.append([cards[i] for i in cur])
                right.append([])
                for i in range(len(cards)):
                    if i not in cur:
                        right[-1].append(cards[i])
                return
            
            for i in range(idx, len(cards)):
                comb(cards, i+1, cur+[i], left, right, length)
        
        def recr(cards):
            if len(cards) == 1:
                return set(cards)
            
            ret = set()
            for length in range(1, len(cards)):
                # get left, right
                left, right = [], []
                comb(cards, 0, [], left, right, length)
                
                for l, r in zip(left, right):
                    for _l in recr(l):
                        for _r in recr(r):
                            for symbol in "+-*/":
                                if not (_r == 0 and symbol == '/'):
                                    ret.add(eval(str(_l) + symbol + str(_r)))
                                if not (_l == 0 and symbol == '/'):
                                    ret.add(eval(str(_r) + symbol + str(_l)))
            return ret
        
        for r in recr(cards):
            if 24 == round(r, 2):
                return True
        return False
