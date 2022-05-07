class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        def next_permutation(cards):
            i = len(cards)-1
            
            while i > 0 and cards[i-1] >= cards[i]:
                i -= 1
            i -= 1
            
            j = i+1
            while j < len(cards) and cards[i] <= cards[j]:
                j += 1
            j -= 1
            
            cards[i], cards[j] = cards[j], cards[i]
            cards[i+1:] = sorted(cards[i+1:])
            return cards
        
        
        def recr(cards):
            if len(cards) == 1:
                return set(cards)
            
            ret = set()
            for i in range(1, len(cards)):
                left = cards[:i]
                right = cards[i:]
                
                for l in recr(left):
                    for r in recr(right):
                        for symbol in ['+', '-', '*', '/']:
                            if not (r == 0 and symbol == '/'):
                                ret.add(eval(str(l) + symbol + str(r)))
                            if not (l == 0 and symbol == '/'):
                                ret.add(eval(str(r) + symbol + str(l)))
            return ret
        
        # loop all permutation
        ans = set()
        cache = set()
        while tuple(cards) not in cache:
            cache.add(tuple(cards))
            
            # check answer
            for p in recr(cards):
                if cards == [8,4,7,1]:
                    ans.add(p)
                if 24 == round(p, 2):
                    return True
            
            cards = next_permutation(cards)
        
        return False
