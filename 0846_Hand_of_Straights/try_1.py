class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        '''
        1. ordereddict
        2. 用hash去紀錄 每個直出現的index => hash[2] = set([1,5])
           sort hand之後，分成再去做交換
        3. hash table
        '''
        
        if len(hand) % groupSize != 0:
            return False
        
        counter = collections.Counter(hand)
        
        for key in sorted(counter.keys()):
            if counter[key] == 0:
                continue
            
            while counter[key] > 0:
                for v in range(key, key+groupSize):
                    if counter[v] <= 0:
                        return False
                    counter[v] -= 1
                
        return True
        