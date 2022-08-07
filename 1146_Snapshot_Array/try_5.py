class SnapshotArray:

    def __init__(self, length: int):
        self.length = length
        self.snap_id = 0
        self.arr = [[[-1, 0]] for _ in range(length)] # (id, val)

    def set(self, index: int, val: int) -> None:
        if self.arr[index][-1][0] == self.snap_id:
            self.arr[index][-1][1] = val
        else:
            self.arr[index].append([self.snap_id, val])

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        j = bisect.bisect_left(self.arr[index], [snap_id + 1,]) - 1
        return self.arr[index][j][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
