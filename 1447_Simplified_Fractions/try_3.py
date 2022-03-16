class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        found = set()
        ans = set()
        
        for i in range(2, n+1):
            for j in range(1, i):
                num = j / i
                if num in found:
                    continue
                
                found.add(num)
                ans.add(f'{j}/{i}')
        return ans