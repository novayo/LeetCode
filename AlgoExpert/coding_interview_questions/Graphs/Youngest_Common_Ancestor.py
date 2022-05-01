'''
main idea: find depth first
time comp: O(d)
space comp: O(1)
- where d is the depth of the tree
'''
# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    # Write your code here.
    d1 = 0
	tmp = descendantOne
	while tmp != topAncestor:
		d1 += 1
		tmp = tmp.ancestor
	
	d2 = 0
	tmp = descendantTwo
	while tmp != topAncestor:
		d2 += 1
		tmp = tmp.ancestor
	
	if d1 < d2:
		descendantOne, descendantTwo = descendantTwo, descendantOne
		d1, d2 = d2, d1
	
	while d1 > d2:
		descendantOne = descendantOne.ancestor
		d1 -= 1
	
	while descendantOne.name != descendantTwo.name:
		descendantOne = descendantOne.ancestor
		descendantTwo = descendantTwo.ancestor
	
	return descendantOne
		

