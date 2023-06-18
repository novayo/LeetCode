class SnapshotArray:

    def __init__(self, length: int):
        self.length = length
        self.snap_id = 0
        self.arr = [[[-1, 0]] for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        if self.snap_id != self.arr[index][-1][0]:
            self.arr[index].append([self.snap_id, 0])
        self.arr[index][-1][1] = val

    def snap(self) -> int:
        ret = self.snap_id
        self.snap_id += 1
        return ret

    def get(self, index: int, snap_id: int) -> int:
        j = bisect.bisect_right(self.arr[index], [snap_id, float('inf')]) - 1
        return self.arr[index][j][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)