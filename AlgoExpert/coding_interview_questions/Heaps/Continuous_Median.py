'''
main idea: heap
time comp: O(logn)
space comp: O(n)
- where n is the length of the inserted number
'''
import heapq

# Do not edit the class below except for
# the insert method. Feel free to add new
# properties and methods to the class.
class ContinuousMedianHandler:
    def __init__(self):
        # Write your code here.
        self.median = None
		self.ascending = []
		self.decending = []

    def insert(self, number):
        # Write your code here.
        heapq.heappush(self.ascending, number)
		
		if len(self.decending) + 1 < len(self.ascending):
			heapq.heappush(self.decending, -heapq.heappop(self.ascending))
		
		if (len(self.ascending) + len(self.decending)) % 2 == 0:
			self.median = (self.ascending[0] + -self.decending[0]) / 2
		else:
			if self.decending:
				self.median = max(self.ascending[0], -self.decending[0])
			else:
				self.median = self.ascending[0]

    def getMedian(self):
        return self.median

