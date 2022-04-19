'''
main idea: recursion
time comp: O(n^2)
space comp: O(n^2)
- where n is the number of nodes in each array, respectively
'''
def sameBsts(arrayOne, arrayTwo):
    # Write your code here.
    n1 = len(arrayOne)
	n2 = len(arrayTwo)
	
	if n1 != n2:
		return False
	if n1 == 0 and n2 == 0:
		return True
	if arrayOne[0] != arrayTwo[0]:
		return False
	
	oneSmall = getSmaller(arrayOne)
	oneBig = getBigger(arrayOne)
	twoSmall = getSmaller(arrayTwo)
	twoBig = getBigger(arrayTwo)
	
	return sameBsts(oneSmall, twoSmall) and sameBsts(oneBig, twoBig)

def getSmaller(array):
	ret = []
	for a in array[1:]:
		if a < array[0]:
			ret.append(a)
	return ret

def getBigger(array):
	ret = []
	for a in array[1:]:
		if a >= array[0]:
			ret.append(a)
	return ret