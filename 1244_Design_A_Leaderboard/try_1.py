
class Leaderboard:

    def __init__(self):
        self.board = collections.defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        self.board[playerId] += score

    # klogk
    def top(self, K: int) -> int:
        heap = []
        for player, score in self.board.items():
            heapq.heappush(heap, (score, player))
            
            if len(heap) > K:
                heapq.heappop(heap)
            
        ans = 0
        for score, player in heap:
            ans += score
        return ans

    def reset(self, playerId: int) -> None:
        del self.board[playerId]


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
