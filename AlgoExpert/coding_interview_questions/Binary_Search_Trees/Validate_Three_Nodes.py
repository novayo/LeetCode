'''
main idea: compare two times
time comp: O(d)
space comp: O(1)
- where d is the distance between nodeOne and nodeThree
'''
# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
    # Write your code here.
	def compare(nodeOne, nodeTwo, nodeThree):
		while nodeOne:
			if nodeOne == nodeTwo:
				break

			if nodeOne.value > nodeTwo.value:
				nodeOne = nodeOne.left
			else:
				nodeOne = nodeOne.right

		if nodeOne != nodeTwo:
			return False

		while nodeTwo:
			if nodeTwo == nodeThree:
				break

			if nodeTwo.value > nodeThree.value:
				nodeTwo = nodeTwo.left
			else:
				nodeTwo = nodeTwo.right

		return nodeTwo == nodeThree
	
	return compare(nodeOne, nodeTwo, nodeThree) or compare(nodeThree, nodeTwo, nodeOne)