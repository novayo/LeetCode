class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        def next_permutation(cards):
            # find first smaller
            i = 3
            while i > 0 and cards[i-1] >= cards[i]:
                i -= 1
            
            if i == 0:
                cards.reverse()
                return
            i -= 1
            
            # find last bigger
            j = i+1
            while j < 4 and cards[j] > cards[i]:
                j += 1
            j -= 1
            
            # swap & reverse
            cards[i], cards[j] = cards[j], cards[i]
            cards[i+1:] = reversed(cards[i+1:])
        
        def recr(i, j, cards):
            if i == j:
                return set([cards[i]])
            
            ret_set = set()
            for k in range(i, j):
                left_set = recr(i, k, cards)
                right_set = recr(k+1, j, cards)
                
                for l_val in left_set:
                    for r_val in right_set:
                        ret_set.add(l_val + r_val)
                        ret_set.add(l_val - r_val)
                        ret_set.add(l_val * r_val)
                        if r_val != 0:
                            ret_set.add(l_val / r_val)
            return ret_set
        
        for _ in range(24):
            next_permutation(cards)
            for val in recr(0, 3, cards):
                if 24 == round(val, 5):
                    return True
        return False