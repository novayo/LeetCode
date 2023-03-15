class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = collections.Counter()
        que = collections.deque()

        for i, _s in enumerate(s):
            counter[_s] += 1

            if counter[_s] > 1: 
                # 整理que
                while que and counter[que[-1][0]] > 1:
                    que.pop()
            else:
                que.appendleft((_s, i))

        if not que:
            return -1
        return que[-1][1]
