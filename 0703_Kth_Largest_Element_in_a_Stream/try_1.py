class MinHeap:
    def __init__(self, nums):
        self.arr = nums
        self.heapifyAll()
    
    def getLength(self):
        return len(self.arr)
    
    def peak(self):
        return self.arr[0]
    
    def push(self, val):
        self.arr.append(val)
        self.heapifyAll()
    
    def pop(self):
        self.arr[0], self.arr[-1] = self.arr[-1], self.arr[0]
        val = self.arr.pop()
        self.heapifyAll()
        return val
    
    def heapifyAll(self):
        for i in range(len(self.arr) // 2, -1, -1):
            self.heapify(i)
    
    def heapify(self, i):
        left = i * 2
        right = i * 2+1
        smallest_index = i
        
        if left < len(self.arr) and self.arr[smallest_index] > self.arr[left]:
            smallest_index = left
        
        if right < len(self.arr) and self.arr[smallest_index] > self.arr[right]:
            smallest_index = right
        
        if smallest_index != i:
            self.arr[smallest_index], self.arr[i] = self.arr[i], self.arr[smallest_index]
            self.heapify(smallest_index)


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = MinHeap(nums)
        
    def add(self, val: int) -> int:
        self.minHeap.push(val)
        
        while self.minHeap.getLength() > self.k:
            self.minHeap.pop()
        
        return self.minHeap.peak()

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)