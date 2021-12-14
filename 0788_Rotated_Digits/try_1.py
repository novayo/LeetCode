class Solution:
    def rotatedDigits(self, n: int) -> int:
        table = {"0":"0", "1":"1", "8":"8", "2":"5", "5":"2", "6":"9", "9":"6"}
        
        numbers = ["0", "1", "2", "5", "6", "8", "9"]
        
        def isValid(string):
            new_string = ''
            for i in range(len(string)):
                new_string += table[string[i]]
                
                if new_string[i] != string[i]:
                    return True
                
            return new_string != string
        
        queue = collections.deque()
        queue.appendleft("")
        ans = max_num = 0
        while max_num <= n:
            cur_num = queue.pop()
            
            for num in numbers:
                tmp = cur_num + num
                
                if tmp[0] == "0":
                    continue
                
                max_num = int(tmp)
                
                if max_num > n:
                    break
                
                if isValid(tmp):
                    ans += 1
                
                queue.appendleft(tmp)
        
        return ans
