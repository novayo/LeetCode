from sortedcontainers import SortedDict

class Leaderboard:

    def __init__(self):
        self.score = SortedDict() # {score: counter}
        self.player = {} # {player: score}

    def addScore(self, playerId: int, score: int) -> None:
        score *= -1
        
        if playerId in self.player:
            ori_score = self.player[playerId]
            new_score = ori_score + score
            
            self.player[playerId] = new_score
            self.score[new_score] = self.score.get(new_score, 0) + 1
            
            val = self.score[ori_score]
            if val == 1:
                del self.score[ori_score]
            else:
                self.score[ori_score] = val - 1
        else:
            self.player[playerId] = score
            self.score[score] = self.score.get(score, 0) + 1
            
    def top(self, K: int) -> int:
        _k = ans = 0
        for score, counter in self.score.items():
            for _ in range(counter):
                ans += -score
                _k += 1
                if _k == K:
                    return ans

    def reset(self, playerId: int) -> None:
        ori_score = self.player[playerId]
        
        del self.player[playerId]
        val = self.score[ori_score]
        if val == 1:
            del self.score[ori_score]
        else:
            self.score[ori_score] = val - 1
        
# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
