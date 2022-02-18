class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        '''
        two pointer + check palindrome => 這樣不夠
        
        我們知道到這裡都一樣之後，只要a的中間是回文(中間的部分就選a) or b的中間是回文(中間的部分就選b)，就會可以組成答案
          |
          v
        ***********
        ***********
                ^
                |
        '''
        def validate(a, b):
            i, j = 0, len(b)-1
            while i < j:
                if a[i] != b[j]:
                    break
                i, j = i+1, j-1

            return a[i:j+1] == a[i:j+1][::-1] or b[i:j+1] == b[i:j+1][::-1]
        
        return validate(a, b) or validate(b, a)
