class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        '''
        dictionary = {persons: 票數}
        list = [(time, 當前最大票數的人是誰(recent))]
        '''
        def findMaxInDict(votes):
            ret_p, cur_max = -1, -1
            
            for p, vote in votes.items():
                if vote >= cur_max:
                    cur_max = vote
                    ret_p = p
            return ret_p
        
        
        votes = collections.OrderedDict()
        self.time_list = []
        
        for p, time in zip(persons, times):
            if p not in votes:
                votes[p] = 0
            votes[p] += 1
            votes.move_to_end(p)
            self.time_list.append((time, findMaxInDict(votes)))
        
        
    def q(self, t: int) -> int:
        '''
        binary search => time, 當前最大票數的人是誰(recent)
        '''
        index = self.bisect_left(self.time_list, t)
        if index >= len(self.time_list):
            return self.time_list[-1][1]
        elif self.time_list[index][0] == t:
            return self.time_list[index][1]
        else:
            return self.time_list[index-1][1]

    def bisect_left(self, list, key):
        l, r = 0, len(list)-1
        
        ans = -1
        while l <= r:
            mid = r - (r-l) // 2
            if list[mid][0] < key:
                l = mid + 1
            elif list[mid][0] == key:
                ans = mid
                r = mid - 1
            else:
                r = mid - 1
                
        return ans if ans > -1 else l
        
        
# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
