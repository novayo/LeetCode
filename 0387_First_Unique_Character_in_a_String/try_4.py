class Solution:
    def firstUniqChar(self, s: str) -> int:
        found_set = set()
        found_many_set = set()
        que = collections.deque()
        
        for i, _s in enumerate(s):
            if _s not in found_set:
                found_set.add(_s)
                que.appendleft(i)
            else:
                found_many_set.add(_s)
                while que and s[que[-1]] == _s:
                    que.pop()
        
        while que and s[que[-1]] in found_many_set:
            que.pop()
        
        return -1 if len(que) == 0 else que[-1]
