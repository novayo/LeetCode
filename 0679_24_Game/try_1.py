class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        
        def recr(cards):
            if len(cards) == 1:
                return 24 == round(cards[0], 2)
            
            for i in range(len(cards)):
                for j in range(i+1, len(cards)):
                    # get next_cards
                    next_cards = []
                    for k in range(len(cards)):
                        if k not in [i, j]:
                            next_cards.append(cards[k])
                    
                    # loop 4 symbols
                    for symbol in ['+', '-', '*', '/']:
                        if not (cards[j] == 0 and symbol == '/') and \
                           recr(next_cards + [eval(str(cards[i]) + symbol + str(cards[j]))]):
                            return True
                        if not (cards[i] == 0 and symbol == '/') and \
                           recr(next_cards + [eval(str(cards[j]) + symbol + str(cards[i]))]):
                            return True
            return False
        
        return recr(cards)
