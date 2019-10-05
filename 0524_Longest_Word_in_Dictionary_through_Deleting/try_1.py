class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        _list, ans = [0]*len(d), collections.deque()
        for value_s in s:
            for index_d, value_d in enumerate(d):
                if _list[index_d] == len(value_d):
                    continue
                if value_d[_list[index_d]] == value_s:
                    _list[index_d] += 1
                if _list[index_d] == len(value_d):
                    ans.append(value_d)
        return max(sorted(ans), key=len) if len(ans) != 0 else ""
