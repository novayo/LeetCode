def radixSort(array):
    # Write your code here.
	if len(array) == 0:
		return array
	
	maxNumber = max(array)
	digit = 0
	
	while maxNumber / pow(10, digit) > 0:
		array = countingSort(array, digit)
		digit += 1
	
    return array

def countingSort(array, digit):
	feq = [[] for _ in range(10)]
	
	for i in range(len(array)):
		idx = array[i] // pow(10, digit) % 10
		feq[idx].append(array[i])
	
	ret = []
	for f in feq:
		ret += f
	return ret

