'''
main idea: ordereddict
insertKeyValuePair: O(1) O(1)
getValueFromKey: O(1) O(1)
getMostRecentKey: O(1) O(1)
'''
import collections

# Do not edit the class below except for the insertKeyValuePair,
# getValueFromKey, and getMostRecentKey methods. Feel free
# to add new properties and methods to the class.
class LRUCache:
    def __init__(self, maxSize):
        self.maxSize = maxSize or 1
		self.od = collections.OrderedDict()

    def insertKeyValuePair(self, key, value):
        # Write your code here.
        if key in self.od:
			self.od.move_to_end(key)
		self.od[key] = value
		if len(self.od) > self.maxSize:
			self.od.popitem(last=False)
		
    def getValueFromKey(self, key):
        # Write your code here.
		if key not in self.od:
			return None
		self.od.move_to_end(key)
        return self.od[key]

    def getMostRecentKey(self):
        # Write your code here.
        k, v = self.od.popitem()
		self.od[k] = v
		return k
