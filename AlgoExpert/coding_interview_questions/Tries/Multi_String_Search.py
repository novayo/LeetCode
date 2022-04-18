'''
main idea: search
time comp: O(nsb)
space comp: O(n)
- where n is the number of smallStrings, s is the length of longest small string , and b is the lenght of the big string
'''
def multiStringSearch(bigString, smallStrings):
    # Write your code here.
    return [s in bigString for s in smallStrings]
