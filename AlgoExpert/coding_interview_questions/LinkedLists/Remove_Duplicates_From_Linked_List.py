'''
main idea: linkedlist
time comp: O(n)
space comp: O(1)
- where n is number of nodes in the linkedlist
'''
# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here.
	head = tmp = linkedList
	
	while tmp and tmp.next:
		if tmp.value == tmp.next.value:
			tmp.next = tmp.next.next
		else:
			tmp = tmp.next
	
	tmp.next = None
    return head

