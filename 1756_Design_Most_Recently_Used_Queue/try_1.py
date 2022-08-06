from sortedcontainers import SortedList

class MRUQueue:

    def __init__(self, n: int):
        self.sd = SortedList()
        self.idx = 0
        
        for i in range(1, n+1):
            self.sd.add((self.idx, i))
            self.idx += 1

    def fetch(self, k: int) -> int:
        ori_idx, ori_task = self.sd[k-1]
        self.sd.remove((ori_idx, ori_task))
        self.idx += 1
        self.sd.add((self.idx, ori_task))
        return ori_task

# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)
