class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        sentence1 = sentence1.split(' ')
        sentence2 = sentence2.split(' ')
        
        n1 = len(sentence1)
        n2 = len(sentence2)
        
        if n1 > n2:
            sentence1, sentence2 = sentence2, sentence1
            n1, n2 = n2, n1
        
        deq1 = collections.deque(sentence1)
        deq2 = collections.deque(sentence2)
        
        while deq1 and deq1[0] == deq2[0]:
            deq1.popleft()
            deq2.popleft()
        
        while deq1 and deq1[-1] == deq2[-1]:
            deq1.pop()
            deq2.pop()
        
        return not deq1 or not deq2