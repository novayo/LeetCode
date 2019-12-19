class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0 or len(tasks) == 1: return len(tasks)
        counter = collections.Counter(tasks)
        counter2 = collections.Counter(counter.values())
        tmp = (max(counter.values()) - 1) * (n + 1) + counter2[max(counter2.keys())]
        return tmp if tmp > len(tasks) else len(tasks)
