'''
main idea: dfs
time comp: O(4^n * n)
space comp: O(4^n * n)
- where n is hte length of the phone number
'''
def phoneNumberMnemonics(phoneNumber):
    # Write your code here.
	graph = {
		"0": ["0"],
		"1": ["1"],
		"2": ["a", "b", "c"],
		"3": ["d", "e", "f"],
		"4": ["g", "h", "i"],
		"5": ["j", "k", "l"],
		"6": ["m", "n", "o"],
		"7": ["p", "q", "r", "s"],
		"8": ["t", "u", "v"],
		"9": ["w", "x", "y", "z"]
	}
	
	def dfs(i):
		if i >= len(phoneNumber):
			return [""]
		
		ret = []
		for s in dfs(i+1):
			for a in graph[phoneNumber[i]]:
				ret.append(a+s)
		return ret
	
    return dfs(0)
