class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0: return len(tasks)
        idles = len(tasks)
        counter = collections.Counter(tasks)
        
        count = 0
        while True:
            if max(counter.values()) == 0: 
                idles -= n-(count-1)
                break
            count = 0
            for k in sorted(counter, key=counter.get, reverse=True):
                if counter[k] == 0 or count == n+1:
                    break
                else:
                    counter[k] -= 1
                    count += 1
            if count < n+1:
                idles += n-(count-1)
        
        return idles
