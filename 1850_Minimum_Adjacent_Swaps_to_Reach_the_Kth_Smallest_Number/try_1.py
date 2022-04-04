class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        o_num = num
        
        # find kth num
        for _ in range(k):
            i = len(num) - 1
            
            while i > 0 and num[i-1] >= num[i]:
                i -= 1
            i -= 1
            
            j = i+1
            while j < len(num) and num[j] > num[i]:
                j += 1
            j -= 1
            
            num = num[:i] + num[j] + ''.join(sorted(num[i+1:j] + num[i] + num[j+1:]))
        
        # bfs find min swap
        found = set([o_num])
        container = set([o_num])
        layer = 0
        
        while container:
            next_container = set()
            
            for n in container:
                if n == num:
                    return layer
                
                for i in range(len(n)-1):
                    t = n[:i] + n[i+1] + n[i] + n[i+2:]
                    if t not in found:
                        next_container.add(t)
                        found.add(t)
                        
            container = next_container
            layer += 1
