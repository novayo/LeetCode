class MaxHeap:
	def __init__(self, array):
		# Do not edit the line below.
		self.heap = array	
		self.heapify()

	# O(n) / O(1)
	def heapify(self):
		# Write your code here.
		for i in range((len(self.heap)) // 2, -1, -1):
			self.siftDown(i)

	# O(logn) / O(1)
	def pop(self):
		# Write your code here.
		self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
		ret = self.heap.pop()
		self.siftDown(0)
		return ret

	# O(logn) / O(1)
	def push(self, value):
		# Write your code here.
		self.heap.append(value)
		self.siftUp(len(self.heap)-1)

	def siftDown(self, startIdx):
		# Write your code here.
		child1 = startIdx * 2 + 1
		while child1 <=  len(self.heap)-1:
			child2 = startIdx * 2 + 2 if startIdx * 2 + 2 <= len(self.heap)-1 else -1
			if child2 != -1 and self.heap[child1] < self.heap[child2]:
				idx = child2
			else:
				idx = child1
			
			if self.heap[startIdx] < self.heap[idx]:
				self.heap[startIdx], self.heap[idx] = self.heap[idx], self.heap[startIdx]
				startIdx = idx
				child1 = startIdx * 2 + 1
			else:
				break

	def siftUp(self, startIdx):
		# Write your code here.
		parent =  (startIdx - 1) // 2
		while startIdx > 0 and self.heap[parent] < self.heap[startIdx]:
			self.heap[parent], self.heap[startIdx] = self.heap[startIdx], self.heap[parent]
			startIdx = parent
			parent =  (startIdx - 1) // 2

# Compared with heapq
import heapq
import random
def gen_random_array():
	length = random.randint(1, 1000)
	arr = []
	for i in range(length):
		arr.append(random.randint(1, 1000))
	return arr

for i in range(1000):
	arr = gen_random_array()
	n = len(arr)
	my_heap = MaxHeap(arr.copy())
	ans_heap = [-v for v in arr.copy()]
	heapq.heapify(ans_heap)

	for _ in range(n):
		v1 = my_heap.pop()
		v2 = -heapq.heappop(ans_heap)
		if v1 != v2:
			print('Bad...')
			break


