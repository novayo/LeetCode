class SnapshotArray:

    def __init__(self, length: int):
        self.arr = [[[-1, 0]] for _ in range(length)]
        self.times = 0

    def set(self, index: int, val: int) -> None:
        self.arr[index].append([self.times, val])

    def snap(self) -> int:
        self.times += 1
        return self.times - 1

    def get(self, index: int, snap_id: int) -> int:
        # 要找最右邊的
        # [[-1, 0], [0, 4], [0, 16], [0, 13]] => 需回傳13 => 因此，找0+1最後index再-1
        i = bisect.bisect_left(self.arr[index], [snap_id+1,])-1
        return self.arr[index][i][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
