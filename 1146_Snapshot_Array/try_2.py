class SnapshotArray:

    def __init__(self, length: int):
        self.arr = collections.defaultdict(int)
        self.times = 0
        self.snapshot = {}

    def set(self, index: int, val: int) -> None:
        self.arr[index] = val

    def snap(self) -> int:
        self.snapshot[self.times] = self.arr.copy()
        self.times += 1
        return self.times - 1

    def get(self, index: int, snap_id: int) -> int:
        return self.snapshot[snap_id][index]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
