'''
main idea: min heap
buildHeap: O(n) / O(1)
siftDown: O(logn) / O(1)
siftUp: O(logn) / O(1)
peek: O(1) / O(1)
remove: O(logn) / O(1)
insert: O(logn) / O(1)
- where n is the length of the input array
'''
# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = array
		self.buildHeap()

    def buildHeap(self):
        # Write your code here.
		for i in range((len(self.heap)-2) // 2, -1, -1):
			self.siftDown(i)

    def siftDown(self, startIdx):
        # Write your code here.
        child1 = startIdx * 2 + 1
		while child1 <=  len(self.heap)-1:
			child2 = startIdx * 2 + 2 if startIdx * 2 + 2 <= len(self.heap)-1 else -1
			if child2 != -1 and self.heap[child1] > self.heap[child2]:
				idx = child2
			else:
				idx = child1
			
			if self.heap[startIdx] > self.heap[idx]:
				self.heap[startIdx], self.heap[idx] = self.heap[idx], self.heap[startIdx]
				startIdx = idx
				child1 = startIdx * 2 + 1
			else:
				break

    def siftUp(self, startIdx):
        # Write your code here.
        parent =  (startIdx - 1) // 2
		while startIdx > 0 and self.heap[parent] > self.heap[startIdx]:
			self.heap[parent], self.heap[startIdx] = self.heap[startIdx], self.heap[parent]
			startIdx = parent
			parent =  (startIdx - 1) // 2

    def peek(self):
        # Write your code here.
        return self.heap[0]

    def remove(self):
        # Write your code here.
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
		ret = self.heap.pop()
		self.siftDown(0)
		return ret

    def insert(self, value):
        # Write your code here.
        self.heap.append(value)
		self.siftUp(len(self.heap)-1)

