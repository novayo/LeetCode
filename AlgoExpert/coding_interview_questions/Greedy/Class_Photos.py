'''
main idea: sort
time comp: O(nlogn)
space comp: O(1)
- where n is the length of the input array
'''
def classPhotos(redShirtHeights, blueShirtHeights):
    # Write your code here.
	redShirtHeights.sort()
	blueShirtHeights.sort()
	
	if redShirtHeights[0] > blueShirtHeights[0]:
		redShirtHeights, blueShirtHeights = blueShirtHeights, redShirtHeights
	
	for r, b in zip(redShirtHeights, blueShirtHeights):
		if r >= b:
			return False
    return True

