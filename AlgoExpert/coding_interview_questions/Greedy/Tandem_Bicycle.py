'''
main idea: sort
time comp: O(nlogn)
space comp: O(1)
- where n is the length of the input array
'''
def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    # Write your code here.
	redShirtSpeeds.sort()
	blueShirtSpeeds.sort(reverse=fastest)
	ret = 0
	for r, b in zip(redShirtSpeeds, blueShirtSpeeds):
		ret += max(r, b)
    return ret

