class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        '''
        找出連續最長的兩種arr
        
        # time complexity: O(n)
        # space complexity: O(n)
        two pointer
        i, j各一種 => 當遇到第三種時
            * i => k（可以用stack, 每次變了紀錄第一次變的index）~ j-1 (只保留第一種到j的)
        '''
        
        ans = 0
        i = j = 0
        
        index = [0]
        found = set()
        while j < len(fruits):
            
            while j < len(fruits):
                found.add(fruits[j])
                if len(found) >= 3:
                    break
                if len(found) == 2 and fruits[j-1] != fruits[j]:
                    index.append(j)
                    flag = False
                j += 1
            
            ans = max(ans, j-i)
            i = index[-1]
            found.remove(fruits[i-1])
        
        return ans
