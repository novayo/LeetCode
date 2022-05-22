'''
main idea: split
time comp: O(1)
space comp: O(1)
'''

def validIPAddresses(string):
    # Write your code here.
	n = len(string)
	
	ans = []
	for i in range(n-2):
		target1 = string[:i+1]
		if int(target1) > 255 or (len(target1) > 1 and target1[0] == '0'):
			break
		
		for j in range(i+1, n-1):
			target2 = string[i+1:j+1]
			if int(target2) > 255 or (len(target2) > 1 and target2[0] == '0'):
				break
				
			for k in range(j+1, n):
				target3 = string[j+1: k+1]
				if int(target3) > 255 or (len(target3) > 1 and target3[0] == '0'):
					break
				
				target4 = string[k+1:]
				if not target4 or int(target4) > 255 or (len(target4) > 1 and target4[0] == '0'):
					continue
				
				ans.append(target1 + '.' + target2 + '.' + target3 + '.' + target4)
    return ans

