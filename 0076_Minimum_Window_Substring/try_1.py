class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter = collections.defaultdict(int)
        loop = {}
        for _t in t:
            counter[_t] += 1
            loop[_t] = 0

        
        ans = ""
        queue = collections.deque()
        j = 0
        
        while j < len(s):

            if s[j] in loop:
                loop[s[j]] += 1
                queue.append(j)
            
            while True:
                flag = True
                for k in loop:
                    if loop[k] < counter[k]:
                        flag = False
                        break

                if flag:
                    i = queue.popleft()
                    if ans == "" or j+1-i < len(ans):
                        ans = s[i:j+1]
                    loop[s[i]] -= 1
                else:
                    break
            j += 1
        
        return ans
