'''
main idea: reverse
time comp: O(n)
space comp: O(n)
- where n is the length of the input string
'''
def isPalindrome(string):
    # Write your code here.
    return string == string[::-1]

