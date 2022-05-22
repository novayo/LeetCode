'''
main idea: split
time comp: O(n)
space comp: O(n)
- where n is the length of the input string
'''

def reverseWordsInString(string):
    # Write your code here.
    return ' '.join(string.split(' ')[::-1])

