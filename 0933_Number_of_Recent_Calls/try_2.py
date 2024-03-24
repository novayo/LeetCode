class RecentCounter:

    def __init__(self):
        self.que = collections.deque()

    def ping(self, t: int) -> int:
        self.que.append(t)

        while self.que and self.que[-1] - self.que[0] > 3000:
            self.que.popleft()
        
        return len(self.que)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)