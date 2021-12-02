class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        '''
        only vote a ticket at one time       
        so we are able to use a variable to store leader
        '''
        leader = None
        counter = collections.defaultdict(int)
        self.time_list = []
        
        for p, t in zip(persons, times):
            counter[p] += 1
            if leader == None or counter[p] >= counter[leader]:
                leader = p
                
            self.time_list.append((t, leader))

    def q(self, t: int) -> int:
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
                l = mid+1
            elif list[mid][0] == key:
                ans = mid
                r = mid-1
            else:
                r = mid-1
        
        return ans if ans > -1 else l


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
