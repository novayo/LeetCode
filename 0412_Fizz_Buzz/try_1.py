class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(1, n+1):
            ans.append("")
            
            if i % 3 == 0:
                ans[-1] += "Fizz"
                
            if i % 5 == 0:
                ans[-1] += "Buzz"
            
            if ans[-1] == "":
                ans[-1] += str(i)
        return ans
