'''
main idea: ptr
time comp: O(n+m)
space comp: O(1)
- where n and m is the number of nodes in linkedlist respectively
'''
# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergeLinkedLists(headOne, headTwo):
    # Write your code here.
	if not headOne:
		return headTwo
	if not headTwo:
		return headOne
	
	if headOne.value > headTwo.value:
		headOne, headTwo = headTwo, headOne
	
    ptr = headOne
	l1 = headOne.next
	l2 = headTwo
    while l1 and l2:
		if l1.value <= l2.value:
			ptr.next = l1
			l1 = l1.next
		else:
			ptr.next = l2
			l2 = l2.next
		ptr = ptr.next
	
	if l1:
		ptr.next = l1
	if l2:
		ptr.next = l2
	return headOne