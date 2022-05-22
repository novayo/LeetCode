'''
main idea: ascii
time comp: O(n)
space comp: O(n)
- where n is the length of the input string
'''
def caesarCipherEncryptor(string, key):
    # Write your code here.
	ans = ''
	key = key % 26
    for s in string:
		ans += chr((ord(s)-ord('a')+key) % 26 + ord('a'))
	return ans

