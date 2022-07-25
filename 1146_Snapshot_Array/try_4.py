import bisect
class SnapshotArray:

    def __init__(self, length: int):
        self.snap_id = 0
        self.table = {}
        for idx in range(length):
            self.table[idx] = [[0,0]]

    def set(self, index: int, val: int) -> None:
        if self.table[index][-1][0] == self.snap_id:
            self.table[index][-1][1] = val
        else:
            self.table[index].append([self.snap_id, val])

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id-1

    def get(self, index: int, snap_id: int) -> int:
        i = bisect.bisect_left(self.table[index], [snap_id+1,]) - 1
        return self.table[index][i][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
