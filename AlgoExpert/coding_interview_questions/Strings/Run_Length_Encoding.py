'''
main idea: count
time comp: O(n)
space comp: O(n)
- where n is the length of the input string
'''
def runLengthEncoding(string):
    # Write your code here.
    ans = ""
	cur_string = ''
	cur_num = 0
	for s in string:
		if s != cur_string:
			while cur_num > 0:
				if cur_num < 10:
					ans += str(cur_num) + cur_string
				else:
					ans += '9' + cur_string
				cur_num -= 9
			cur_string = s
			cur_num = 1
		else:
			cur_num += 1
	
	while cur_num > 0:
		if cur_num < 10:
			ans += str(cur_num) + cur_string
		else:
			ans += '9' + cur_string
		cur_num -= 9
	return ans
